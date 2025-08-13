import unittest
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "../templates")

class TestHTMLFiles(unittest.TestCase):

    def test_home_html_exists(self):
        self.assertTrue(os.path.exists(os.path.join(TEMPLATE_DIR, "home.html")), "home.html is missing")

    def test_play_computer_html_exists(self):
        self.assertTrue(os.path.exists(os.path.join(TEMPLATE_DIR, "play_computer.html")), "play_computer.html is missing")

    def test_play_friends_html_exists(self):
        self.assertTrue(os.path.exists(os.path.join(TEMPLATE_DIR, "play_friends.html")), "play_friends.html is missing")

    def test_home_html_has_title(self):
        with open(os.path.join(TEMPLATE_DIR, "home.html"), "r") as f:
            content = f.read()
        self.assertIn("<title>", content)
        self.assertIn("</title>", content)

    def test_play_computer_has_div(self):
        with open(os.path.join(TEMPLATE_DIR, "play_computer.html"), "r") as f:
            content = f.read()
        self.assertIn("<div", content)

    def test_play_friends_has_script_or_form(self):
        with open(os.path.join(TEMPLATE_DIR, "play_friends.html"), "r") as f:
            content = f.read()
        self.assertTrue("<script" in content or "<form" in content)

if __name__ == '__main__':
    unittest.main()

