import os
from pathlib import Path
import onnxruntime as ort
import numpy as np
from PIL import Image

class Manual:
    def __init__(self):
        self.model_path = 'best.onnx'
        self.session = ort.InferenceSession(self.model_path)
        self.input_name = self.session.get_inputs()[0].name
        self.class_names = ["Boston", "Chicago", "LosAngeles", "Phoenix", "WashingtonDC"]
        print("Manual class instantiated")

    def classify_image(self, image_path):
        img = Image.open(image_path).resize((224, 224))
        img_array = np.array(img).astype(np.float32) / 255.0  # Normalize the image
        img_array = img_array.transpose(2, 0, 1)  # Convert to (C, H, W)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        outputs = self.session.run(None, {self.input_name: img_array})
        prediction = outputs[0][0]
        class_id = np.argmax(prediction)
        return self.class_names[class_id]

    def classify_images(self, image_paths):
        for image_path in image_paths:
            class_name = self.classify_image(image_path)
            folder_path = os.path.dirname(image_path)
            class_folder = os.path.join(folder_path, class_name)
            Path(class_folder).mkdir(parents=True, exist_ok=True)
            new_image_path = os.path.join(class_folder, os.path.basename(image_path))
            os.rename(image_path, new_image_path)
            print(f"Moved {image_path} to {new_image_path}")
