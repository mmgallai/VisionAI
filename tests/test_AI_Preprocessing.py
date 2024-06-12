import unittest
import numpy as np
from PIL import Image
import os
import sys
from unittest.mock import patch

# Ensure the root directory is in the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.AI import AI

class TestAIPreprocessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_image_path = 'test images/image1.jpg'
        cls.ai = AI(None, 'test images')

    @patch('onnxruntime.InferenceSession.run', return_value=[np.array([[0, 1, 0, 0, 0]])])
    @patch('PIL.Image.open')
    def test_preprocessing(self, mock_open, mock_run):
        # Create a dummy image array
        img_array = np.random.rand(224, 224, 3).astype(np.float32)
        img = Image.fromarray((img_array * 255).astype(np.uint8))

        # Set up the mock to return the dummy image
        mock_open.return_value = img

        # Manually preprocess the dummy image
        img = img.resize((224, 224))
        expected_img_array = np.array(img).astype(np.float32) / 255.0  # Normalize
        expected_img_array = expected_img_array.transpose(2, 0, 1)  # Convert to (C, H, W)
        expected_img_array = np.expand_dims(expected_img_array, axis=0)  # Add batch dimension

        # Print the manually preprocessed array
        print("Manually preprocessed array:\n", expected_img_array[0][0])

        # Call the classify_image method
        self.ai.classify_image(self.test_image_path)

        # Extract the actual preprocessed image array passed to the model
        actual_img_array = mock_run.call_args[0][1][self.ai.input_name]

        # Print the array from classify_image method
        print("Array from classify_image method:\n", actual_img_array[0][0])

        # Check if preprocessing is done correctly
        np.testing.assert_array_almost_equal(expected_img_array, actual_img_array, decimal=5, err_msg="Preprocessing not done correctly")

if __name__ == '__main__':
    unittest.main()
