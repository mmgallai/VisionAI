from PyQt5.QtWidgets import QDialog, QFileDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class InitialFolderSelection(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Initial Folder")
        self.setFixedSize(500, 300) 
        self.setStyleSheet("background-color: #2b2b2b; color: white;")
        
        self.layout = QVBoxLayout(self)
        
        self.label = QLabel("Please select the folder where you want to save your albums:", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setWordWrap(True)  # text to wrap
        
        self.select_button = QPushButton("Select Folder", self)
        self.select_button.setStyleSheet(
            """
            QPushButton {
                border: 2px solid #3EB489; 
                color: white;
                font-size: 20px;
                padding: 10px;
                border-radius: 10px;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: #3EB489;
            }
            """
        )
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.select_button, alignment=Qt.AlignCenter)
        
        self.select_button.clicked.connect(self.select_folder)
        
    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.selected_folder = folder_path
            self.accept()
        else:
            self.selected_folder = None
