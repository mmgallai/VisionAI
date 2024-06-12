from PyQt5.QtWidgets import QDialog, QFileDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from view.ButtonStyle import ButtonStyle  # Import ButtonStyle

class InitialFolderSelection(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Initial Folder")
        self.setFixedSize(500, 300)
        self.setStyleSheet("background-color: #2b2b2b; color: white; font-family: Consolas;")
        
        self.layout = QVBoxLayout(self)
        
        self.label = QLabel("Please select the folder where you want to save your albums:", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 20px; font-family: Consolas;")
        self.label.setWordWrap(True)
        
        self.select_button = QPushButton("Select Folder", self)
        self.select_button.setStyleSheet(ButtonStyle.get_default_style())
        
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
