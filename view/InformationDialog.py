from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt
from view.ButtonStyle import ButtonStyle

class InformationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Information")
        self.setFixedSize(600, 700)
        self.setStyleSheet("background-color: #2b2b2b; color: white; font-family: Consolas; font-size: 20px;")

        self.layout = QVBoxLayout(self)
        
        self.info_label = QLabel(
            "This software allows you to organize images using Vision AI or manually.\n"
            "Features include:\n"
            "1. Selecting a folder to display its contents.\n"
            "2. Navigation through history with back and forward buttons.\n"
            "3. Sorting folders by the number of images they contain.\n"
            "4. Viewing single images on double-click.\n"
            "5. Clicking 'Vision AI' will create albums for their respective folders.\n"
            "6. Selecting 'Manual' will allow you to selectively create albums for particular images, including the option to select multiple images.\n"
            "\n"
            "Instructions:\n"
            "1. Select 'Select Folder' to choose a directory.\n"
            "2. Use 'Select Method' to choose Vision AI or Manual classification.\n"
            "3. Navigate through folders using 'Back' and 'Forward' buttons.\n"
            "4. View web demo to check model performance and working, hosted on Hugging Face.\n"
            "5. The number of images in the current folder is displayed at the bottom right corner.\n"
            "6. The current directory path is displayed at the bottom right corner, just above the number of images.\n"
        )
        self.info_label.setStyleSheet("font-size: 18px; font-family: Consolas;")
        self.info_label.setWordWrap(True)
        self.layout.addWidget(self.info_label)

        self.ok_button = QPushButton("OK")
        self.ok_button.setStyleSheet(ButtonStyle.get_default_style())
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button, alignment=Qt.AlignCenter)

        self.center_on_screen()

    def center_on_screen(self):
        screen_geometry = QDesktopWidget().availableGeometry().center()
        self.move(screen_geometry.x() - self.width() // 2, screen_geometry.y() - self.height() // 2)
