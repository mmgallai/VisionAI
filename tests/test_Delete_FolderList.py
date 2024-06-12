# Author ~ Abdu Raziq
import os
import sys
from unittest.mock import MagicMock, patch
import shutil
import pytest
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

# Import the module containing the class to be tested
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from view.FolderList import FolderList

# Initialize QApplication before running any tests
app = QApplication(sys.argv)

@pytest.fixture
def folder_list(qtbot):
    parent = MockParent()
    folder_list = FolderList(parent)
    qtbot.addWidget(parent)  # Ensure the parent widget is not garbage collected
    return folder_list

# it ensures that if an exception is raised during the folder deletion process, the appropriate error message is displayed to the user.

def test_delete_folder_error(folder_list, qtbot):
    # Mock folder_path and parent
    folder_path = '/path/to/folder'
    folder_list.parent = MagicMock()

    # This ensures that the application correctly handles the error by displaying an appropriate error message to the user.
    # Patch QMessageBox.question to return Yes and shutil.rmtree to raise an exception
    with patch.object(QMessageBox, 'question', return_value=QMessageBox.Yes):
        with patch('shutil.rmtree', side_effect=Exception('Test error')):
            with patch.object(QMessageBox, 'warning') as mock_warning:
                # Call delete_folder method
                folder_list.delete_folder(folder_path)
                qtbot.wait(50)  # Ensure the event loop has time to process
                # Assertions
                mock_warning.assert_called_once()

class MockParent(QWidget):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()  # Create a QWidget instance as the central widget
        self.frame_settings = MagicMock()  # Mock the frame_settings attribute

# Run the tests using pytest.main()
if __name__ == '__main__':
    pytest.main(['-v', __file__])
