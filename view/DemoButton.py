from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
import webbrowser

class DemoButton(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton("Try Web Demo", self)
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

        self.button.clicked.connect(self.try_demo)

    def try_demo(self):
        webbrowser.open("https://huggingface.co/spaces/jagruthh/cities_small")
        print("Web demo initiated")
