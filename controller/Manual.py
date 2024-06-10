from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox, QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from PyQt5.QtCore import Qt
from view.ButtonStyle import ButtonStyle  # Import ButtonStyle
import os
from pathlib import Path
import onnxruntime as ort
import numpy as np
from PIL import Image

class Manual:
    def __init__(self, parent, initial_directory):
        self.parent = parent
        self.initial_directory = initial_directory
        self.model_path = os.path.join('model', 'best.onnx')
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

    def classify_images(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilters(["Image files (*.png *.jpg *.jpeg *.bmp)"])
        if file_dialog.exec_():
            image_paths = file_dialog.selectedFiles()
            if image_paths:
                self.select_album(image_paths)

    def select_album(self, image_paths):
        albums = [f.name for f in Path(self.initial_directory).iterdir() if f.is_dir()]
        if not albums:
            QMessageBox.information(self.parent, "No Albums Found", "No albums found. Please create a new album.", QMessageBox.Ok)
            self.create_new_album(image_paths)
        else:
            album_dialog = QDialog(self.parent)
            album_dialog.setWindowTitle("Select Album")
            album_dialog.setStyleSheet("background-color: #2b2b2b; color: white; font-family: Consolas;")
            album_dialog.setFixedSize(400, 200)

            layout = QVBoxLayout(album_dialog)
            label = QLabel("Choose an album or create a new one:", album_dialog)
            label.setStyleSheet("font-size: 16px; font-family: Consolas;")
            layout.addWidget(label)

            album_combo = QComboBox(album_dialog)
            album_combo.addItems(albums + ["Create new album"])
            layout.addWidget(album_combo)

            button = QPushButton("OK", album_dialog)
            button.setStyleSheet(ButtonStyle.get_default_style())  # Use ButtonStyle
            layout.addWidget(button)
            button.clicked.connect(lambda: self.handle_album_selection(album_combo, image_paths, album_dialog))
            album_dialog.exec_()

    def handle_album_selection(self, album_combo, image_paths, album_dialog):
        album = album_combo.currentText()
        if album == "Create new album":
            self.create_new_album(image_paths)
        else:
            self.save_images_to_album(image_paths, album)
        album_dialog.accept()

    def create_new_album(self, image_paths):
        album_dialog = QDialog(self.parent)
        album_dialog.setWindowTitle("Create New Album")
        album_dialog.setStyleSheet("background-color: #2b2b2b; color: white; font-family: Consolas;")
        album_dialog.setFixedSize(400, 200)

        layout = QVBoxLayout(album_dialog)
        label = QLabel("Enter the name of the new album:", album_dialog)
        label.setStyleSheet("font-size: 16px; font-family: Consolas;")
        layout.addWidget(label)

        album_input = QLineEdit(album_dialog)
        layout.addWidget(album_input)

        button = QPushButton("Create", album_dialog)
        button.setStyleSheet(ButtonStyle.get_default_style())  # Use ButtonStyle
        layout.addWidget(button)
        button.clicked.connect(lambda: self.handle_new_album_creation(album_input, image_paths, album_dialog))
        album_dialog.exec_()

    def handle_new_album_creation(self, album_input, image_paths, album_dialog):
        album_name = album_input.text()
        if album_name:
            album_path = os.path.join(self.initial_directory, album_name)
            Path(album_path).mkdir(parents=True, exist_ok=True)
            self.save_images_to_album(image_paths, album_name)
            self.parent.update_view(self.initial_directory)
            album_dialog.accept()
        else:
            QMessageBox.warning(self.parent, "Error", "Album name cannot be empty.", QMessageBox.Ok)

    def save_images_to_album(self, image_paths, album_name):
        album_path = os.path.join(self.initial_directory, album_name)
        for image_path in image_paths:
            new_image_path = os.path.join(album_path, os.path.basename(image_path))
            os.rename(image_path, new_image_path)
            print(f"Moved {image_path} to {new_image_path}")
        QMessageBox.information(self.parent, "Success", f"Images have been saved to the album '{album_name}'.", QMessageBox.Ok)
