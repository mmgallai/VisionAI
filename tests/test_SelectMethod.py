import unittest
from unittest.mock import MagicMock
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from view.SelectMethod import SelectMethod

class TestSelectMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.dialog = SelectMethod(None)  # Initialize without a parent for testing

    def tearDown(self):
        self.dialog.close()

    def test_dialog_initialization(self):
        # Test the title of the dialog
        self.assertEqual(self.dialog.windowTitle(), "Choose Classification Method")

        # Test the fixed size of the dialog
        self.assertEqual(self.dialog.size().width(), 500)
        self.assertEqual(self.dialog.size().height(), 250)

        # Test the stylesheet of the dialog
        self.assertEqual(self.dialog.styleSheet(), "background-color: #2b2b2b; color: white;")

        # Test the label text
        expected_label_text = "Do you want to classify the photos using Vision AI or manually?"
        self.assertEqual(self.dialog.label.text(), expected_label_text)

        # Test the label stylesheet
        self.assertEqual(self.dialog.label.styleSheet(), "color: white; font-size: 18px; font-family: Consolas;")

        # Test the buttons' existence and styles
        self.assertIsInstance(self.dialog.vision_ai_button, QPushButton)
        self.assertIsInstance(self.dialog.manual_button, QPushButton)
        self.assertEqual(self.dialog.vision_ai_button.styleSheet(), self.dialog.manual_button.styleSheet())

    def test_button_connections(self):
        # Check that the vision_ai_button is connected to the use_vision_ai method
        self.dialog.vision_ai_button.clicked.connect(self.dialog.use_vision_ai)
        self.assertTrue(self.dialog.vision_ai_button.receivers(self.dialog.vision_ai_button.clicked) > 0)

        # Check that the manual_button is connected to the use_manual method
        self.dialog.manual_button.clicked.connect(self.dialog.use_manual)
        self.assertTrue(self.dialog.manual_button.receivers(self.dialog.manual_button.clicked) > 0)

if __name__ == '__main__':
    unittest.main()