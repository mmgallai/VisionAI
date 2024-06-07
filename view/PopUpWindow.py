from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from controller.AI import AI
from controller.Manual import Manual

class PopUpWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.folder_path = None
        self.setWindowTitle("Choose Classification Method")
        self.setStyleSheet("background-color: black;")
        
        self.label = QLabel("Do you want to classify the photos using Vision AI or manually?", self)
        self.label.setStyleSheet("color: white; font-size: 18px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        
        self.vision_ai_button = QPushButton("Vision AI", self)
        self.vision_ai_button.setStyleSheet(
            """
            QPushButton {
                border: 4px solid #3EB489; /* Mint color */
                color: white;
                font-family: 'shanti';
                font-size: 18px;
                border-radius: 15px;
                padding: 10px 20px;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: #3EB489; /* Mint color on hover */
            }
            """
        )
        
        self.manual_button = QPushButton("Manually", self)
        self.manual_button.setStyleSheet(
            """
            QPushButton {
                border: 4px solid #3EB489; /* Mint color */
                color: white;
                font-family: 'shanti';
                font-size: 18px;
                border-radius: 15px;
                padding: 10px 20px;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: #3EB489; /* Mint color on hover */
            }
            """
        )
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.vision_ai_button)
        self.layout.addWidget(self.manual_button)
        
        self.setLayout(self.layout)
        self.setFixedSize(500, 250)
        
        self.vision_ai_button.clicked.connect(self.use_vision_ai)
        self.manual_button.clicked.connect(self.use_manual)

    def set_folder_path(self, folder_path):
        self.folder_path = folder_path

    def use_vision_ai(self):
        if self.folder_path:
            ai_instance = AI()
            ai_instance.classify_folder(self.folder_path)
        self.accept()

    def use_manual(self):
        if self.folder_path:
            manual_instance = Manual()
            manual_instance.classify_folder(self.folder_path)
        self.accept()
