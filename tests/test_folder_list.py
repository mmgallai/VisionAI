import os
import unittest
from unittest.mock import MagicMock, patch

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox  # Import QMessageBox directly
from PyQt5.QtWidgets import QWidget
from view.FolderList import FolderList


class TestFolderList(unittest.TestCase):

    def setUp(self):
        self.folder_list = FolderList(MockParent())

    @patch('PyQt5.QtWidgets.QMessageBox.question', return_value=QMessageBox.Yes)
    @patch('PyQt5.QtWidgets.QMessageBox.information')
    @patch('shutil.rmtree')
    def test_delete_folder_confirmation_yes(self, mock_rmtree, mock_information, mock_question):
        # Mock folder_path and parent
        folder_path = '/path/to/folder'
        self.folder_list.parent = MagicMock()
        
        # Call delete_folder method
        self.folder_list.delete_folder(folder_path)
        
        # Assertions
        mock_question.assert_called_once()
        mock_rmtree.assert_called_once_with(folder_path)
        mock_information.assert_called_once_with(self.folder_list, 'Success', 'Folder deleted successfully!')

    @patch('PyQt5.QtWidgets.QMessageBox.question', return_value=QMessageBox.No)
    @patch('PyQt5.QtWidgets.QMessageBox.information')
    @patch('shutil.rmtree')
    def test_delete_folder_confirmation_no(self, mock_rmtree, mock_information, mock_question):
        # Mock folder_path and parent
        folder_path = '/path/to/folder'
        self.folder_list.parent = MagicMock()
        
        # Call delete_folder method
        self.folder_list.delete_folder(folder_path)
        
        # Assertions
        mock_question.assert_called_once()
        mock_rmtree.assert_not_called()
        mock_information.assert_not_called()

    @patch('PyQt5.QtWidgets.QMessageBox.question', return_value=QMessageBox.Yes)
    @patch('PyQt5.QtWidgets.QMessageBox.warning')
    @patch('shutil.rmtree', side_effect=Exception('Test error'))
    def test_delete_folder_error(self, mock_rmtree, mock_warning, mock_question):
        # Mock folder_path and parent
        folder_path = '/path/to/folder'
        self.folder_list.parent = MagicMock()
        
        # Call delete_folder method
        self.folder_list.delete_folder(folder_path)
        
        # Assertions
        mock_question.assert_called_once()
        mock_rmtree.assert_called_once_with(folder_path)
        mock_warning.assert_called_once()
    

class MockParent(QWidget):
    def __init__(self):
        super().__init__()
        self.central_widget = MagicMock()




if __name__ == '__main__':
    unittest.main()
