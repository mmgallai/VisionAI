import unittest
import os

class TestIconsExist(unittest.TestCase):
    def test_icons_exist(self):
        script_dir = os.path.dirname(__file__)
        icons_dir = os.path.join(script_dir, "..", "icons")
        icon_files = [
            "back_icon.png",
            "demo_icon.png",
            "directories_icon.png",
            "folder_icon.png",
            "forward_icon.png",
            "image_icon.png",
            "info_icon.png",
            "method_icon.png",
            "sort_icon.png",
            "delete_icon.png"
        ]

        for icon in icon_files:
            icon_path = os.path.join(icons_dir, icon)
            with self.subTest(icon=icon):
                self.assertTrue(os.path.isfile(icon_path), f"Icon file {icon} does not exist")

if __name__ == '__main__':
    unittest.main()