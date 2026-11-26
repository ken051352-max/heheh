"""Install into temporary user homes; do not touch the actual agent configuration."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("install_tutor", ROOT / "tools/install_tutor.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class TutorInstaller(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.home = Path(temporary.name).resolve()

    def install(self, **kwargs):
        return installer.install(ROOT, self.home, environ={}, **kwargs)

    def test_fresh_install_binds_checkout_and_does_not_copy_private_state(self):
        result = self.install()
        skill = Path(result["skill"])
        self.assertEqual(json.loads((skill / "local.json").read_text())["roadmap_root"], str(ROOT))
        self.assertEqual((skill / "scripts/progress.py").read_bytes(),
                         (ROOT / "resources/tutor/roadmap-tutor/scripts/progress.py").read_bytes())
        self.assertTrue(Path(result["opencode_agent"]).is_file())
        native = Path(result["opencode_skill"])
        for name in installer.SKILL_FILES + ("local.json",):
            self.assertEqual((native / name).read_bytes(), (skill / name).read_bytes())
        self.assertFalse((self.home / "study-private").exists())
        self.assertEqual({str(p.relative_to(skill)).replace("\\", "/") for p in skill.rglob("*") if p.is_file()},
                         set(installer.SKILL_FILES) | {"local.json"})

    def test_identical_install_is_a_noop(self):
        self.install()
        result = self.install()
        self.assertEqual(result["written_files"], 0)
        self.assertIsNone(result["backup"])

    def test_conflict_preflight_leaves_other_destinations_untouched(self):
        agent = self.home / ".config/opencode/agents/roadmap-tutor.md"
        agent.parent.mkdir(parents=True)
        agent.write_text("My existing agent", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Existing file differs"):
            self.install()
        self.assertFalse((self.home / ".agents/skills/roadmap-tutor").exists())
        self.assertEqual(agent.read_text(), "My existing agent")

    def test_update_backs_up_changed_files_and_preserves_other_configuration(self):
        result = self.install()
        agent = Path(result["opencode_agent"])
        agent.write_text("My customized tutor", encoding="utf-8")
        config = self.home / ".config/opencode/local-settings.json"
        config.write_text('{"keep":true}', encoding="utf-8")
        unknown = Path(result["skill"]) / "my-note.txt"
        unknown.write_text("keep this", encoding="utf-8")
        updated = self.install(update=True)
        self.assertEqual(updated["written_files"], 1)
        backup = Path(updated["backup"])
        self.assertEqual((backup / "0-roadmap-tutor.md").read_text(), "My customized tutor")
        self.assertEqual(json.loads((backup / "index.json").read_text()), [str(agent)])
        self.assertEqual(config.read_text(), '{"keep":true}')
        self.assertEqual(unknown.read_text(), "keep this")

    def test_custom_config_requires_explicit_destination(self):
        with self.assertRaisesRegex(ValueError, "Custom OpenCode"):
            installer.install(ROOT, self.home, environ={"XDG_CONFIG_HOME": str(self.home / "custom")})
        target = self.home / "custom/opencode"
        result = installer.install(ROOT, self.home, opencode_dir=target,
                                   environ={"XDG_CONFIG_HOME": str(self.home / "custom")})
        self.assertEqual(Path(result["opencode_agent"]), target / "agents/roadmap-tutor.md")
        self.assertFalse((self.home / ".config/opencode").exists())

    def test_invalid_repository_does_not_install(self):
        with self.assertRaisesRegex(ValueError, "roadmap checkout"):
            installer.install(self.home, self.home, environ={})
        self.assertFalse((self.home / ".agents").exists())


if __name__ == "__main__":
    unittest.main()
