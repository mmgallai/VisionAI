import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QListWidget, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import os

class PhotoOrganizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.albums = {}

    def initUI(self):
        self.setWindowTitle('Photo Organizer')
        self.setGeometry(100, 100, 800, 600)
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)
        self.layout = QVBoxLayout()
        self.uploadButton = QPushButton('Upload Photos', self)
        self.uploadButton.clicked.connect(self.upload_photos)
        self.layout.addWidget(self.uploadButton)
        self.albumList = QListWidget()
        self.layout.addWidget(self.albumList)
        self.albumNameInput = QLineEdit(self)
        self.albumNameInput.setPlaceholderText('New Album Name')
        self.layout.addWidget(self.albumNameInput)
        self.createAlbumButton = QPushButton('Create Album', self)
        self.createAlbumButton.clicked.connect(self.create_album)
        self.layout.addWidget(self.createAlbumButton)
        self.summaryLabel = QLabel('Album Summary', self)
        self.layout.addWidget(self.summaryLabel)
        self.mainWidget.setLayout(self.layout)

    def upload_photos(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "Upload Photos", "", "Images Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        if files:
            for file in files:
                self.classify_photo(file)

    def classify_photo(self, file):
        album_name = "Default Album"
        if album_name not in self.albums:
            self.albums[album_name] = []
        self.albums[album_name].append(file)
        self.update_album_list()

    def create_album(self):
        album_name = self.albumNameInput.text()
        if album_name and album_name not in self.albums:
            self.albums[album_name] = []
            self.albumNameInput.clear()
            self.update_album_list()
        else:
            QMessageBox.warning(self, 'Error', 'Album name cannot be empty or duplicate.')

    def update_album_list(self):
        self.albumList.clear()
        for album_name, photos in self.albums.items():
            self.albumList.addItem(f"{album_name} ({len(photos)} photos)")
        self.update_summary()

    def update_summary(self):
        summary = "\n".join([f"{album_name}: {len(photos)} photos" for album_name, photos in self.albums.items()])
        self.summaryLabel.setText(f"Album Summary:\n{summary}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PhotoOrganizer()
    ex.show()
    sys.exit(app.exec_())
