from PyQt5.QtWidgets import QPushButton, QFileDialog, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class UploadButton(QWidget):
    def __init__(self, l_margin=0, r_margin=0, parent=None):
        super().__init__(parent)
        self.button = QPushButton("Upload Photos", self)
        self.button.clicked.connect(self.upload_photos)
        self.button.setStyleSheet(
            f"""
            QPushButton {{
                margin-left: {l_margin}px;
                margin-right: {r_margin}px;
                border: 4px solid '#BC006C';
                color: white;
                font-family: 'shanti';
                font-size: 36px;
                border-radius: 25px;
                padding: 15px 0;
                margin-top: 20px;
            }}
            QPushButton:hover {{
                background-color: '#BC006C';
            }}
            """
        )

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.button)
        
    def upload_photos(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "Upload Photos", "", "Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        if files:
            for file in files:
                self.classify_photo(file)

    def classify_photo(self, file):
        # Placeholder for the photo classification method
        print(f"Classifying photo: {file}")
        # this should give the photos to the model to classify
        # the model should be implemented in the model folder
