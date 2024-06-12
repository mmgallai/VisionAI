import unittest
import os
import sys
from PyQt5.QtWidgets import QApplication

# Ensure the root directory is in the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from view.MainView import MainWindow

class TestImageCount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()

    def setUp(self):
        self.main_window = MainWindow(initial_folder='test images')
        self.main_window.show()
        
        # Override closeEvent to avoid asking for confirmation
        self.main_window.closeEvent = lambda event: event.accept()

    def tearDown(self):
        self.main_window.close()

    def test_image_count(self):
        # Update the view with the test_images folder path
        test_folder = 'test images'
        self.main_window.update_view(test_folder)

        # Get the displayed image count from the label
        actual_image_count_label = self.main_window.button_panel.image_count_label.text()
        actual_image_count = int(actual_image_count_label.split(': ')[1])

        # Get the expected image count by counting the image files in the test_images folder
        image_files = [f for f in os.listdir(test_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        expected_image_count = len(image_files)

        # Verify the image count is correct
        self.assertEqual(actual_image_count, expected_image_count)

if __name__ == '__main__':
    unittest.main()
