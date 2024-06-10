from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class CloseConfirmationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Close Confirmation")
        self.setFixedSize(600, 200)
        self.setStyleSheet("background-color: #2b2b2b; color: white;")

        layout = QVBoxLayout(self)
        
        label = QLabel("Are you sure you want to close the application?", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-family: Consolas; font-size: 20px;")
        layout.addWidget(label)
        
        button_layout = QHBoxLayout()
        
        yes_button = QPushButton("Yes", self)
        yes_button.setStyleSheet(
            """
            QPushButton {
                border: 2px solid #3EB489; 
                color: white;
                font-family: Consolas;
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
        yes_button.clicked.connect(self.accept)
        
        no_button = QPushButton("No", self)
        no_button.setStyleSheet(
            """
            QPushButton {
                border: 2px solid #3EB489; 
                color: white;
                font-family: Consolas;
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
        no_button.clicked.connect(self.reject)
        
        button_layout.addWidget(yes_button)
        button_layout.addWidget(no_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
