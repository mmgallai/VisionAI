import unittest
from PyQt5.QtWidgets import QApplication
import sys
import os
import numpy as np
from PIL import Image

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from view.MainView import MainWindow
from view.SelectMethod import SelectMethod
from controller.AI import AI

class TestAI_PredictedCity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
    
    def setUp(self):
        self.window = MainWindow(initial_folder=".")
        self.select_method = SelectMethod(self.window)
    
    def test_AI_PredictedCity(self):
        ai_instance = AI(self.window, self.window.initial_directory)
        
        # Construct the path to the test image dynamically
        script_dir = os.path.dirname(__file__)
        test_image_path = os.path.join(script_dir, "..", "test images", "image3.jpg") 

        # Ensure the image path exists before running the test
        self.assertTrue(os.path.isfile(test_image_path), f"Test image file does not exist: {test_image_path}")
        
        # Perform classification
        prediction = ai_instance.classify_image(test_image_path)
        
        print(f"Predicted city: {prediction}")

        # Ensure that the predicted city is in the list of class names
        self.assertIn(prediction, ai_instance.class_names, f"The predicted city '{prediction}' is not in the list of expected cities.")
    
    @classmethod
    def tearDownClass(cls):
        del cls.app

if __name__ == '__main__':
    unittest.main()
