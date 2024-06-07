import os
from pathlib import Path
import onnxruntime as ort
import numpy as np
from PIL import Image

class AI:
    def __init__(self):
        self.model_path = 'best.onnx'
        self.session = ort.InferenceSession(self.model_path)
        self.input_name = self.session.get_inputs()[0].name
        self.class_names = ["Boston", "Chicago", "LosAngeles", "Phoenix", "WashingtonDC"]
        print("AI class instantiated")

    def classify_image(self, image_path):
        img = Image.open(image_path).resize((224, 224))
        img_array = np.array(img).astype(np.float32) / 255.0  # Normalize the image
        img_array = img_array.transpose(2, 0, 1)  # Convert to (C, H, W)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        outputs = self.session.run(None, {self.input_name: img_array})
        prediction = outputs[0][0]
        class_id = np.argmax(prediction)
        return self.class_names[class_id]

    def classify_folder(self, folder_path):
        for image_file in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_file)
            if not image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue
            class_name = self.classify_image(image_path)
            class_folder = os.path.join(folder_path, class_name)
            Path(class_folder).mkdir(parents=True, exist_ok=True)
            os.rename(image_path, os.path.join(class_folder, image_file))
