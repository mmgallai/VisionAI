from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from view.PopUpWindow import PopUpWindow

class UploadButton(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton("Select Method", self)
        self.button.clicked.connect(self.show_popup)
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
        
    def show_popup(self):
        popup = PopUpWindow(self)
        popup.exec_()
