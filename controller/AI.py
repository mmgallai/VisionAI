import os
from pathlib import Path
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from view.ButtonStyle import ButtonStyle
import onnxruntime as ort
import numpy as np
from PIL import Image

class AI:
    def __init__(self, parent, initial_directory):
        self.parent = parent
        self.initial_directory = initial_directory 
        self.model_path = os.path.join('model', 'best.onnx')
        self.session = ort.InferenceSession(self.model_path)
        self.input_name = self.session.get_inputs()[0].name
        self.class_names = ["Boston", "Chicago", "LosAngeles", "Phoenix", "WashingtonDC"]
        print("AI class instantiated")

    def classify_image(self, image_path):
        img = Image.open(image_path).resize((224, 224))
        img_array = np.array(img).astype(np.float32) / 255.0  # Normalize
        img_array = img_array.transpose(2, 0, 1)  # Convert to (C, H, W)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        outputs = self.session.run(None, {self.input_name: img_array})
        prediction = outputs[0][0]
        class_id = np.argmax(prediction)
        return self.class_names[class_id]

    def classify_files(self, image_paths):
        for image_path in image_paths:
            class_name = self.classify_image(image_path)
            class_folder = os.path.join(self.initial_directory, class_name)
            Path(class_folder).mkdir(parents=True, exist_ok=True)
            new_image_path = os.path.join(class_folder, os.path.basename(image_path))
            os.rename(image_path, new_image_path)
            print(f"Moved {image_path} to {new_image_path}")
        self.show_success_message("Success", "Images have been classified and moved to their respective folders.")

    def show_success_message(self, title, message):
        success_dialog = QDialog(self.parent)
        success_dialog.setWindowTitle(title)
        success_dialog.setStyleSheet("background-color: #2b2b2b; color: white; font-family: Consolas; font-size: 20px;")
        success_dialog.setFixedSize(450, 160)

        layout = QVBoxLayout(success_dialog)
        label = QLabel(message, success_dialog)
        label.setStyleSheet("font-size: 20px; font-family: Consolas;")
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        button = QPushButton("OK", success_dialog)
        button.setStyleSheet(ButtonStyle.get_default_style())
        layout.addWidget(button)
        button.clicked.connect(success_dialog.accept)
        
        success_dialog.exec_()
