from PyQt5.QtWidgets import QPushButton, QFileDialog, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class UploadButton(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton("Upload Photos", self)
        self.button.clicked.connect(self.upload_photos)
        self.button.setStyleSheet(
            """
            QPushButton {
                border: 4px solid #3EB489; /* Mint color */
                color: white;
                font-family: 'shanti';
                font-size: 36px;
                border-radius: 25px;
                padding: 15px 30px; /* Increased padding for a larger button */
                background-color: transparent; /* Transparent background */
            }
            QPushButton:hover {
                background-color: #3EB489; /* Mint color on hover */
            }
            """
        )

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
        
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
