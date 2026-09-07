from pathlib import Path
import unittest
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "profile" / "README.md"
ROOT_README = ROOT / "README.md"
SETUP = ROOT / "SETUP.md"
LIGHT_MARK = ROOT / "assets" / "aster-mark-light.png"
DARK_MARK = ROOT / "assets" / "aster-mark-dark.png"


class ProfileRepositoryTests(unittest.TestCase):
    def test_required_public_files_exist(self):
        for path in (PROFILE, ROOT_README, SETUP, LIGHT_MARK, DARK_MARK):
            self.assertTrue(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")

    def test_profile_has_core_brand_copy(self):
        text = PROFILE.read_text(encoding="utf-8")
        self.assertIn("Aster Clinical™", text)
        self.assertIn("Practical software for everyday clinical work.", text)
        self.assertIn("independent doctors", text)
        self.assertIn("small clinics", text)
        self.assertNotIn("Aster Clinical®", text)

    def test_profile_links_current_public_work(self):
        text = PROFILE.read_text(encoding="utf-8")
        self.assertIn("https://github.com/AsterClinical/brand-assets", text)
        self.assertIn("https://github.com/AsterClinical/clinical-document-platform-format", text)
        self.assertIn("https://asterclinical.com/", text)
        self.assertIn("admin@asterclinical.com", text)

    def test_profile_uses_theme_aware_local_marks(self):
        text = PROFILE.read_text(encoding="utf-8")
        self.assertIn("prefers-color-scheme: dark", text)
        self.assertIn("../assets/aster-mark-dark.png", text)
        self.assertIn("../assets/aster-mark-light.png", text)

    def test_profile_avoids_badge_and_stats_clutter(self):
        text = PROFILE.read_text(encoding="utf-8").lower()
        self.assertNotIn("shields.io", text)
        self.assertNotIn("github-readme-stats", text)
        self.assertNotIn("visitor", text)

    def test_marks_are_rgba_and_nonempty(self):
        for path in (LIGHT_MARK, DARK_MARK):
            im = Image.open(path)
            self.assertEqual(im.mode, "RGBA")
            self.assertGreaterEqual(im.width, 256)
            self.assertGreaterEqual(im.height, 256)
            alpha = im.getchannel("A")
            self.assertGreater(alpha.getextrema()[1], 0)

    def test_python_cache_files_are_ignored(self):
        ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("__pycache__/", ignore)
        self.assertIn("*.pyc", ignore)

    def test_setup_contains_exact_pinning_guidance(self):
        text = SETUP.read_text(encoding="utf-8")
        self.assertIn("brand-assets", text)
        self.assertIn("clinical-document-platform-format", text)
        self.assertIn("Practical clinical software for independent doctors and small clinics.", text)
        self.assertIn("Customize pins", text)


if __name__ == "__main__":
    unittest.main()
