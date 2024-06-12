from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from view.ButtonStyle import ButtonStyle

class CloseConfirmationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Close Confirmation")
        self.setStyleSheet("background-color: #2b2b2b; color: white; font-family: Consolas; font-size: 18px;")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout(self)

        label = QLabel("Are you sure you want to close the application?", self)
        label.setAlignment(Qt.AlignCenter)
        label.setWordWrap(True)
        label.setStyleSheet("font-size: 20px; font-family: Consolas;")
        layout.addWidget(label)

        button_layout = QHBoxLayout()

        yes_button = QPushButton("Yes", self)
        yes_button.setStyleSheet(ButtonStyle.get_default_style())
        yes_button.clicked.connect(self.accept)
        button_layout.addWidget(yes_button)

        no_button = QPushButton("No", self)
        no_button.setStyleSheet(ButtonStyle.get_default_style())
        no_button.clicked.connect(self.reject)
        button_layout.addWidget(no_button)

        layout.addLayout(button_layout)
