import unittest
from unittest.mock import MagicMock
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from view.InformationDialog import InformationDialog

class TestInformationDialog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.dialog = InformationDialog()

    def tearDown(self):
        self.dialog.close()

    def test_dialog_properties(self):
        # Verify the title of the dialog
        self.assertEqual(self.dialog.windowTitle(), "Information")
        
        # Verify the fixed size of the dialog
        self.assertEqual(self.dialog.size().width(), 600)
        self.assertEqual(self.dialog.size().height(), 700)

        # Verify the style sheet
        self.assertEqual(self.dialog.styleSheet(), "background-color: #2b2b2b; color: white; font-family: Consolas; font-size: 20px;")

        # Verify the content of the info label
        expected_text = (
            "This software allows you to organize images using Vision AI or manually.\n"
            "Features include:\n"
            "1. Selecting a folder to display its contents.\n"
            "2. Navigation through history with back and forward buttons.\n"
            "3. Sorting folders by the number of images they contain.\n"
            "4. Viewing single images on double-click.\n"
            "5. Clicking 'Vision AI' will create albums for their respective folders.\n"
            "6. Selecting 'Manual' will allow you to selectively create albums for particular images, including the option to select multiple images.\n"
            "\n"
            "Instructions:\n"
            "1. Select 'Select Folder' to choose a directory.\n"
            "2. Use 'Select Method' to choose Vision AI or Manual classification.\n"
            "3. Navigate through folders using 'Back' and 'Forward' buttons.\n"
            "4. View web demo to check model performance and working, hosted on Hugging Face.\n"
            "5. The number of images in the current folder is displayed at the bottom right corner.\n"
            "6. The current directory path is displayed at the bottom right corner, just above the number of images.\n"
        )
        self.assertEqual(self.dialog.info_label.text(), expected_text)

        # Verify the OK button text
        self.assertEqual(self.dialog.ok_button.text(), "OK")

    def test_dialog_centering(self):
        # Mock the QDesktopWidget to return a specific geometry
        desktop_widget = QApplication.desktop()
        screen_rect = desktop_widget.availableGeometry(desktop_widget.primaryScreen())

        # Calculate the expected position
        expected_x = screen_rect.center().x() - self.dialog.width() // 2
        expected_y = screen_rect.center().y() - self.dialog.height() // 2

        # Verify the position of the dialog
        self.dialog.center_on_screen()
        self.assertEqual(self.dialog.x(), expected_x)
        self.assertEqual(self.dialog.y(), expected_y)

    def test_ok_button_functionality(self):
        # Simulate a click on the OK button
        QTest.mouseClick(self.dialog.ok_button, Qt.LeftButton)
        
        # Since the dialog closes on OK, we can't check `accept` directly;
        # instead, we verify that the dialog is no longer visible
        self.assertFalse(self.dialog.isVisible())

if __name__ == '__main__':
    unittest.main()
