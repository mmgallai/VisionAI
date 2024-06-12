import unittest
import os

class TestModelExist(unittest.TestCase):
    def test_ModelExist(self):
        script_dir = os.path.dirname(__file__)
        model = os.path.join(script_dir, "..", "model", "best.onnx")
        print(f"Looking for model at: {model}")
        self.assertTrue(os.path.isfile(model), "Model file does not exist")

if __name__ == '__main__':
    unittest.main()
