import unittest
from unittest.mock import patch, MagicMock
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import sys
import os

# Ensure the root directory is in the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from view.MainView import MainWindow

class TestMainWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.main_window = MainWindow(initial_folder='test images')
        
        # Override closeEvent to avoid asking for confirmation during tests
        self.main_window.closeEvent = lambda event: event.accept()
        
        self.main_window.show()

    def tearDown(self):
        self.main_window.close()

    @patch('webbrowser.open')
    def test_open_demo(self, mock_open):
        # Call the open_demo method
        self.main_window.open_demo()

        # Check if webbrowser.open was called with the correct URL
        mock_open.assert_called_once_with("https://huggingface.co/spaces/jagruthh/cities_small")

if __name__ == '__main__':
    unittest.main()
