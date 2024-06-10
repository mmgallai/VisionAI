from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
from controller.AI import AI
from controller.Manual import Manual
from view.ButtonStyle import ButtonStyle

class SelectMethod(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Choose Classification Method")
        self.setStyleSheet("background-color: #2b2b2b; color: white;")
        self.setFixedSize(500, 250)

        self.label = QLabel("Do you want to classify the photos using Vision AI or manually?", self)
        self.label.setStyleSheet("color: white; font-size: 18px; font-family: Consolas;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.vision_ai_button = QPushButton("Vision AI", self)
        self.vision_ai_button.setStyleSheet(ButtonStyle.get_default_style())
        self.manual_button = QPushButton("Manually", self)
        self.manual_button.setStyleSheet(ButtonStyle.get_default_style())

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.vision_ai_button)
        self.layout.addWidget(self.manual_button)

        self.setLayout(self.layout)

        self.vision_ai_button.clicked.connect(self.use_vision_ai)
        self.manual_button.clicked.connect(self.use_manual)

    def use_vision_ai(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilters(["Image files (*.png *.jpg *.jpeg *.bmp)"])
        if file_dialog.exec_():
            image_paths = file_dialog.selectedFiles()
            if image_paths:
                ai_instance = AI(self.parent, self.parent.initial_directory)
                ai_instance.classify_files(image_paths)
                self.parent.update_view(self.parent.initial_directory)
        self.accept()
        
    def use_manual(self):
        manual_instance = Manual(self.parent, self.parent.initial_directory)
        manual_instance.classify_images()
        self.accept()
