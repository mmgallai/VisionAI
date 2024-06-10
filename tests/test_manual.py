import unittest
from unittest.mock import patch, MagicMock
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QLineEdit, QMessageBox
from controller.Manual import Manual

class TestManual(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the QApplication instance required for PyQt widgets
        cls.app = QApplication([])

    def setUp(self):
        # Initialize the Manual class with a dummy parent and initial directory
        self.manual = Manual(parent=None, initial_directory="test_directory")

    @patch('PyQt5.QtWidgets.QFileDialog')
    @patch('PyQt5.QtWidgets.QMessageBox')
    def test_handle_empty_album_name(self, mock_message_box, mock_file_dialog):
        # Create a MagicMock to simulate the file dialog behavior
        mock_file_dialog_instance = MagicMock()
        
        # Set up the mock to simulate user selecting multiple image files
        mock_file_dialog_instance.exec_.return_value = QDialog.Accepted
        mock_file_dialog_instance.selectedFiles.return_value = ["image1.jpg", "image2.png"]
        
        # Set the return value of the QFileDialog.getExistingFiles to our mock instance
        mock_file_dialog.return_value = mock_file_dialog_instance
        
        # Simulate the case where the user enters an empty album name
        album_input = MagicMock(spec=QLineEdit)
        album_input.text.return_value = ""

        # Mock the QMessageBox to simulate the warning message
        mock_message_box_instance = MagicMock()
        mock_message_box.return_value = mock_message_box_instance

        # Call the method to be tested
        self.manual.handle_new_album_creation(album_input, ["image1.jpg", "image2.png"], QDialog())
        
        # Verify that the warning message box is shown when album name is empty
        mock_message_box.assert_called_once()
        mock_message_box_instance.setText.assert_called_once_with("Album name cannot be empty.")
        mock_message_box_instance.exec_.assert_called_once()

if __name__ == '__main__':
    unittest.main()
