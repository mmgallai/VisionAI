import unittest
from PyQt5.QtWidgets import QApplication
import sys
import os
import numpy as np
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from view.MainView import MainWindow
from view.SelectMethod import SelectMethod
from controller.AI import AI

class TestAI_NumberOfOutputs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
    
    def setUp(self):
        self.window = MainWindow(initial_folder=".")
        self.select_method = SelectMethod(self.window)
    
    def test_AI_Method_NumberOfOutputs(self):
        # Ensure the model path is correct and the file exists
        ai_instance = AI(self.window, self.window.initial_directory)
        self.assertTrue(os.path.isfile(ai_instance.model_path), f"Model file does not exist: {ai_instance.model_path}")
        
        # Construct the path to the test image dynamically
        script_dir = os.path.dirname(__file__)
        test_image_path = os.path.join(script_dir, "..", "test images", "image1.jpg") 

        # Ensure the image path exists before running the test
        self.assertTrue(os.path.isfile(test_image_path), f"Test image file does not exist: {test_image_path}")
        
        # Perform classification
        prediction = ai_instance.classify_image(test_image_path)
        
        # Print prediction for debugging
        print(f"Prediction: {prediction}")

        # Verify the prediction length
        self.assertEqual(len(prediction), 6, "The prediction should have 6 elements")  # Adjust if needed
    
    @classmethod
    def tearDownClass(cls):
        del cls.app

if __name__ == '__main__':
    unittest.main()
