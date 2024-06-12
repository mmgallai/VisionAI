from PyQt5.QtWidgets import QFileDialog, QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from PyQt5.QtCore import Qt
from view.ButtonStyle import ButtonStyle  # Import ButtonStyle
import os
from pathlib import Path

class Manual:
    def __init__(self, parent, initial_directory):
        self.parent = parent
        self.initial_directory = initial_directory
        print("Manual class instantiated")

    def classify_images_manually(self):
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
            self.show_warning_message("No Albums Found", "No albums found. Please create a new album.")
            self.create_new_album(image_paths)
        else:
            album_dialog = QDialog(self.parent)
            album_dialog.setWindowTitle("Select Album")
            album_dialog.setStyleSheet("background-color: #2b2b2b; color: white; font-family: Consolas; font-size: 20px;")
            album_dialog.setFixedSize(500, 300)

            layout = QVBoxLayout(album_dialog)
            label = QLabel("Choose an album or create a new one:", album_dialog)
            label.setStyleSheet("font-size: 20px; font-family: Consolas; ")
            label.setWordWrap(True)
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
        album_dialog.setStyleSheet("background-color: #2b2b2b; color: white; font-family: Consolas; font-size: 20px;")
        album_dialog.setFixedSize(450, 180)  # Increased size to show all label text

        layout = QVBoxLayout(album_dialog)
        label = QLabel("Enter the name of the new album:", album_dialog)
        label.setStyleSheet("font-size: 20px; font-family: Consolas;")
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
            self.show_warning_message("Error", "Album name cannot be empty.")

    def save_images_to_album(self, image_paths, album_name):
        album_path = os.path.join(self.initial_directory, album_name)
        for image_path in image_paths:
            new_image_path = os.path.join(album_path, os.path.basename(image_path))
            if not os.path.exists(new_image_path):
                os.rename(image_path, new_image_path)
                print(f"Moved {image_path} to {new_image_path}")
            else:
                # File exists, add a suffix to the filename
                base, ext = os.path.splitext(new_image_path)
                counter = 1
                new_image_path_with_suffix = f"{base}_{counter}{ext}"
                while os.path.exists(new_image_path_with_suffix):
                    counter += 1
                    new_image_path_with_suffix = f"{base}_{counter}{ext}"
                os.rename(image_path, new_image_path_with_suffix)
                print(f"Moved {image_path} to {new_image_path_with_suffix}")
        self.show_success_message("Success", f"Images have been saved to the album '{album_name}'.")

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

    def show_warning_message(self, title, message):
        warning_dialog = QDialog(self.parent)
        warning_dialog.setWindowTitle(title)
        warning_dialog.setStyleSheet("background-color: #2b2b2b; color: white; font-family: Consolas; font-size: 20px;")
        warning_dialog.setFixedSize(400, 200)

        layout = QVBoxLayout(warning_dialog)
        label = QLabel(message, warning_dialog)
        label.setStyleSheet("font-size: 20px; font-family: Consolas;")
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        button = QPushButton("OK", warning_dialog)
        button.setStyleSheet(ButtonStyle.get_default_style())
        layout.addWidget(button)
        button.clicked.connect(warning_dialog.accept)
        
        warning_dialog.exec_()
