#!/usr/bin/env python3
"""Validate markdown links in the repo.

Default mode (used by CI, must stay fast and offline):
  1. relative file targets exist;
  2. #anchors resolve in the target file, using GitHub's rules:
     explicit <a id="..."> tags OR heading-derived slugs
     (lowercase, strip punctuation/emoji, spaces->hyphens, dedupe with -1, -2).
  Exit code 1 on any internal failure.

Optional external mode (network; report-only unless --strict-external):
  python3 tools/check_links.py --external [--paths curriculum coursepages ...]
                               [--report audit/external.md] [--strict-external]
  Checks every http(s) URL found in markdown links and <autolinks>.
  Classification:
    OK    2xx/3xx after following redirects
    WARN  401/403/405/429/999 (bot-gated or rate-limited; usually fine in a browser)
    FAIL  404/410/other 4xx, 5xx, DNS/connection/timeout errors
  Redirects that land on a different host are listed so moved courses can be reviewed.
"""
import argparse
import http.cookiejar
import concurrent.futures
import glob
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MD_FILES = [p for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
            if "/node_modules/" not in p and not p.endswith("README.md.orig")]

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
AUTOLINK = re.compile(r"<(https?://[^>\s]+)>")
AID = re.compile(r'<a id="([^"]+)"></a>')
HEADING = re.compile(r"^(#{1,6})\s+(.*)$", re.M)


def github_slug(text):
    # strip markdown emphasis and links, keep link text
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("*", "").replace("`", "")
    out = []
    for ch in text.strip().lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in (" ", "-"):
            out.append("-")
        elif unicodedata.category(ch).startswith(("L", "N")):
            out.append(ch)
        # else drop (punctuation, emoji, symbols)
    return "".join(out)  # github keeps consecutive hyphens


def anchors_of(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    anchors = set(AID.findall(text))
    counts = {}
    # strip fenced code blocks so '#' comments aren't headings
    text_noc = re.sub(r"```.*?```", "", text, flags=re.S)
    for m in HEADING.finditer(text_noc):
        s = github_slug(m.group(2))
        n = counts.get(s, 0)
        counts[s] = n + 1
        anchors.add(s if n == 0 else "%s-%d" % (s, n))
    return anchors


def check_internal():
    anchors_cache = {p: anchors_of(p) for p in MD_FILES}
    fails = 0
    checked = 0
    for p in MD_FILES:
        with open(p, encoding="utf-8") as f:
            text = f.read()
        # also check <img src="...">
        targets = LINK.findall(text) + re.findall(r'src="([^"]+)"', text)
        for t in targets:
            if t.startswith(("http://", "https://", "mailto:")):
                continue
            if "…" in t:  # prose placeholder (e.g. `src="assets/…"` in audit docs)
                continue
            checked += 1
            if t.startswith("#"):
                fpath, anchor = p, t[1:]
            else:
                part = t.split("#", 1)
                rel_file = part[0]
                anchor = part[1] if len(part) > 1 else None
                fpath = os.path.normpath(os.path.join(os.path.dirname(p), rel_file))
                if not os.path.exists(fpath):
                    print("MISSING FILE  %s -> %s" % (os.path.relpath(p, ROOT), t))
                    fails += 1
                    continue
                if anchor is None or os.path.isdir(fpath):
                    continue
                if not fpath.endswith(".md"):
                    continue
            if fpath not in anchors_cache:
                anchors_cache[fpath] = anchors_of(fpath)
            if anchor not in anchors_cache[fpath]:
                print("BAD ANCHOR    %s -> %s (in %s)" % (os.path.relpath(p, ROOT), t,
                                                          os.path.relpath(fpath, ROOT)))
                fails += 1
    print("\nchecked %d internal links across %d md files; %d failures" %
          (checked, len(MD_FILES), fails))
    return fails


# ----------------------------------------------------------------- external
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36 heheh-link-checker")
WARN_CODES = {401, 403, 405, 429, 999}
# Hosts that block every non-browser client; never treat as dead.
BOT_GATED_HOSTS = ("x.com", "twitter.com", "linkedin.com", "www.linkedin.com",
                   "medium.com", "openai.com", "www.coursera.org")


def collect_external(paths):
    files = []
    for rel in paths:
        full = os.path.join(ROOT, rel)
        if os.path.isfile(full):
            files.append(full)
        else:
            files.extend(glob.glob(os.path.join(full, "**", "*.md"), recursive=True))
    urls = {}
    for p in sorted(set(files)):
        with open(p, encoding="utf-8") as f:
            text = re.sub(r"```.*?```", "", f.read(), flags=re.S)
        for u in LINK.findall(text) + AUTOLINK.findall(text):
            if not u.startswith(("http://", "https://")):
                continue
            u = u.rstrip(".,;")
            urls.setdefault(u, set()).add(os.path.relpath(p, ROOT))
    return urls


def probe(url, timeout):
    """Return (status_label, http_code_or_error, final_url)."""
    last_err = None
    # cookie-aware opener: some sites (e.g. milvus.io) set a cookie then redirect
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={
            "User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
            "Accept-Language": "en"})
        try:
            with opener.open(req, timeout=timeout) as r:
                return "OK", r.status, r.geturl()
        except urllib.error.HTTPError as e:
            last_err = e.code
            if method == "HEAD" and e.code in (400, 403, 404, 405, 429, 500, 501, 503):
                continue  # many servers mishandle HEAD; retry with GET
            break
        except Exception as e:  # DNS, TLS, timeout, connection reset
            last_err = type(e).__name__
            if method == "HEAD":
                continue
            break
    host = urllib.parse.urlparse(url).netloc.lower()
    if isinstance(last_err, int) and (last_err in WARN_CODES or host.endswith(BOT_GATED_HOSTS)):
        return "WARN", last_err, url
    if not isinstance(last_err, int) and host.endswith(BOT_GATED_HOSTS):
        return "WARN", last_err, url
    return "FAIL", last_err, url


def check_external(paths, report, workers, timeout):
    urls = collect_external(paths)
    print("checking %d unique external URLs in %s ..." % (len(urls), ", ".join(paths)))
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(probe, u, timeout): u for u in urls}
        for fut in concurrent.futures.as_completed(futs):
            results[futs[fut]] = fut.result()
    counts = {"OK": 0, "WARN": 0, "FAIL": 0}
    moved = []
    for u, (label, code, final) in results.items():
        counts[label] += 1
        if label == "OK" and urllib.parse.urlparse(final).netloc != urllib.parse.urlparse(u).netloc:
            moved.append((u, final))
    for label in ("FAIL", "WARN"):
        for u in sorted(k for k, v in results.items() if v[0] == label):
            print("%-5s %-6s %s   (%s)" % (label, results[u][1], u, ", ".join(sorted(urls[u]))))
    for u, final in sorted(moved):
        print("MOVED        %s -> %s" % (u, final))
    print("\nexternal: %d OK · %d WARN (bot-gated) · %d FAIL · %d cross-host redirects" %
          (counts["OK"], counts["WARN"], counts["FAIL"], len(moved)))
    if report:
        with open(os.path.join(ROOT, report), "w", encoding="utf-8") as f:
            f.write("# External link report\n\n")
            f.write("Generated by `python3 tools/check_links.py --external`. "
                    "Legend: OK = 2xx/3xx · WARN = 401/403/405/429 (bot-gated) · FAIL = dead.\n\n")
            f.write("**Totals:** %d OK · %d WARN · %d FAIL · %d cross-host redirects\n\n" %
                    (counts["OK"], counts["WARN"], counts["FAIL"], len(moved)))
            f.write("| Status | Code | URL | Found in |\n|---|---|---|---|\n")
            order = {"FAIL": 0, "WARN": 1, "OK": 2}
            for u in sorted(results, key=lambda k: (order[results[k][0]], k)):
                label, code, _ = results[u]
                f.write("| %s | %s | `%s` | %s |\n" % (label, code, u, ", ".join(sorted(urls[u]))))
            if moved:
                f.write("\n## Cross-host redirects (review: course may have moved)\n\n")
                f.write("| Original | Lands on |\n|---|---|\n")
                for u, final in sorted(moved):
                    f.write("| `%s` | `%s` |\n" % (u, final))
        print("report written to", report)
    return counts["FAIL"]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--external", action="store_true",
                    help="also HTTP-check external URLs (needs network)")
    ap.add_argument("--paths", nargs="+",
                    default=["curriculum", "coursepages", "guides", "resources"],
                    help="files/dirs to scan in --external mode")
    ap.add_argument("--report", help="write a markdown report (repo-relative path)")
    ap.add_argument("--strict-external", action="store_true",
                    help="exit 1 if any external URL FAILs")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--timeout", type=float, default=20.0)
    args = ap.parse_args()

    internal_fails = check_internal()
    external_fails = 0
    if args.external:
        print()
        external_fails = check_external(args.paths, args.report, args.workers, args.timeout)
    if internal_fails or (args.strict_external and external_fails):
        sys.exit(1)


if __name__ == "__main__":
    main()
