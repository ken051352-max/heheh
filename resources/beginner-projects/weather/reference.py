"""Worked M1 Weather CLI; fixtures by default, bounded optional HTTP adapter."""
import argparse
from datetime import datetime, timedelta
import json
import math
from pathlib import Path
import sys
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

CITIES = {"delhi": (28.61, 77.21), "london": (51.51, -0.13)}
FIXTURE = Path(__file__).parent / "fixtures" / "current.json"


class WeatherError(ValueError):
    """An error safe to show at the command line."""


def parse_weather(raw: bytes) -> dict:
    try:
        data = json.loads(raw.decode("utf-8"))
        value = data["current"]["temperature_2m"]
        stamp = data["current"]["time"]
        units = data["current_units"]["temperature_2m"]
        if type(value) not in (int, float) or not math.isfinite(value):
            raise ValueError("temperature is not a finite number")
        if not isinstance(stamp, str) or "T" not in stamp:
            raise ValueError("missing timestamp")
        parsed_stamp = datetime.fromisoformat(stamp)
        if parsed_stamp.utcoffset() not in (None, timedelta(0)):
            raise ValueError("expected UTC timestamp")
        if units != "°C":
            raise ValueError("expected Celsius")
    except (ValueError, KeyError, TypeError, UnicodeError) as error:
        raise WeatherError("weather data is malformed or has unexpected fields/units") from error
    return {"temperature_c": float(value), "observed_at_utc": stamp}


def read_cache(path: Path, city: str, now: float, ttl: float) -> dict | None:
    """Missing/corrupt/future/expired caches are misses; exact TTL boundary expires."""
    try:
        entry = json.loads(path.read_text(encoding="utf-8"))
        saved = entry["saved_at"]
        if type(saved) not in (int, float) or not math.isfinite(saved):
            return None
        if entry["city"] != city or not 0 <= now - saved < ttl:
            return None
        # Validate cached payload by the same contract as new provider data.
        return parse_weather(entry["payload"].encode("utf-8"))
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        return None


def write_cache(path: Path, city: str, raw: bytes, now: float) -> None:
    """Replace a complete cache entry; keep the earlier file if writing fails."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=".weather-", suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            json.dump({"city": city, "saved_at": now, "payload": raw.decode("utf-8")}, stream)
        temporary.replace(path)
    except OSError as error:
        raise WeatherError("cannot write cache; choose a writable cache directory") from error
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def download(url: str, timeout: float) -> bytes:
    """One request, no automatic retries; tests inject a fake instead."""
    with urlopen(url, timeout=timeout) as response:
        data = response.read(65_537)
    if len(data) > 65_536:
        raise WeatherError("weather response exceeds the 64 KiB teaching limit")
    return data


def get_weather(city: str, cache_path: Path, *, offline=True, fixture=FIXTURE,
                fetch=download, now=None, ttl=900, timeout=5) -> dict:
    city = city.strip().casefold()
    if city not in CITIES:
        raise WeatherError("unknown city; choose Delhi or London")
    if type(ttl) not in (int, float) or not math.isfinite(ttl) or ttl <= 0:
        raise WeatherError("cache TTL must be finite and positive")
    if type(timeout) not in (int, float) or not math.isfinite(timeout) or timeout <= 0:
        raise WeatherError("timeout must be finite and positive")
    if offline:
        try:
            result = parse_weather(Path(fixture).read_bytes())
        except OSError as error:
            raise WeatherError("cannot read the offline fixture") from error
        return {"city": city, **result, "source": "synthetic fixture"}
    now = time.time() if now is None else now
    result = read_cache(Path(cache_path), city, now, ttl)
    if result is not None:
        return {"city": city, **result, "source": "cache"}
    latitude, longitude = CITIES[city]
    url = "https://api.open-meteo.com/v1/forecast?" + urlencode({
        "latitude": latitude, "longitude": longitude, "current": "temperature_2m",
        "temperature_unit": "celsius", "timezone": "UTC"})
    try:
        raw = fetch(url, timeout)
    except HTTPError as error:
        raise WeatherError(f"weather service returned HTTP {error.code}") from error
    except (URLError, TimeoutError, OSError) as error:
        raise WeatherError("weather request failed or timed out; try offline mode") from error
    result = parse_weather(raw)
    write_cache(Path(cache_path), city, raw, now)
    return {"city": city, **result, "source": "provider"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("city", nargs="?", default="Delhi")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--offline", action="store_true", help="default: use synthetic fixture")
    mode.add_argument("--live", action="store_true", help="opt in to one Open-Meteo request")
    parser.add_argument("--cache", type=Path, default=Path("weather-cache.json"))
    parser.add_argument("--fixture", type=Path, default=FIXTURE)
    args = parser.parse_args(argv)
    try:
        result = get_weather(args.city, args.cache, offline=not args.live, fixture=args.fixture)
    except WeatherError as error:
        print(f"Weather unavailable: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
