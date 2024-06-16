import sys
import unittest
from unittest.mock import MagicMock

from PyQt5.QtWidgets import QApplication, QMainWindow


# Mock classes to represent the application structure
class FolderList:
    def __init__(self):
        self.folders = []
        self.images = []

    def add_folder(self, folder_name):
        self.folders.append(folder_name)

    def add_image(self, image_name):
        self.images.append(image_name)

    def sort_folders(self, order="ascending", case_sensitive=True):
        if not case_sensitive:
            self.folders.sort(key=lambda x: x.lower())
            self.images.sort(key=lambda x: x.lower())
        else:
            self.folders.sort()
            self.images.sort()

        if order == "descending":
            self.folders.reverse()
            self.images.reverse()

class ButtonPanel:
    def __init__(self, parent):
        self.sort_button = MagicMock()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.folder_list = FolderList()
        self.button_panel = ButtonPanel(self)

class TestSortButton(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.main_window = MainWindow()
        self.button_panel = self.main_window.button_panel
        self.folder_list = self.main_window.folder_list

        # Adding mock folders and images
        self.folder_list.add_folder('FolderC')
        self.folder_list.add_folder('FolderA')
        self.folder_list.add_folder('FolderB')
        self.folder_list.add_image('ImageC.jpg')
        self.folder_list.add_image('ImageA.jpg')
        self.folder_list.add_image('ImageB.jpg')

    def test_sort_button(self):
        # Simulate a click on the sort button
        self.folder_list.sort_folders()

        # Check if folders and images are sorted
        expected_folders = ['FolderA', 'FolderB', 'FolderC']
        expected_images = ['ImageA.jpg', 'ImageB.jpg', 'ImageC.jpg']

        self.assertEqual(self.folder_list.folders, expected_folders)
        self.assertEqual(self.folder_list.images, expected_images)

    def test_sort_ascending(self):
        # Additional test case for ascending order sorting
        self.folder_list.add_folder('')
        self.folder_list.add_image('')
        self.folder_list.sort_folders(order="ascending")

        expected_folders = ['', 'FolderA', 'FolderB', 'FolderC']
        expected_images = ['', 'ImageA.jpg', 'ImageB.jpg', 'ImageC.jpg']

        self.assertEqual(self.folder_list.folders, expected_folders)
        self.assertEqual(self.folder_list.images, expected_images)



    def test_sort_empty_name(self):
        # Additional test case for handling empty folder/image names
        self.folder_list.add_folder('')
        self.folder_list.add_image('')
        self.folder_list.sort_folders(order="ascending")

        expected_folders = ['', 'FolderA', 'FolderB', 'FolderC']
        expected_images = ['', 'ImageA.jpg', 'ImageB.jpg', 'ImageC.jpg']

        self.assertEqual(self.folder_list.folders, expected_folders)
        self.assertEqual(self.folder_list.images, expected_images)

if __name__ == "__main__":
    unittest.main()
