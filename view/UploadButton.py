from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from view.SelectMethod import SelectMethod
from view.ButtonStyle import ButtonStyle  # Import ButtonStyle

class UploadButton(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.folder_path = None
        self.button = QPushButton("Select Method", self)
        self.button.clicked.connect(self.show_popup)
        self.button.setStyleSheet(ButtonStyle.get_large_style())  # Use ButtonStyle

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
        
    def setFolderPath(self, folder_path):
        self.folder_path = folder_path

    def show_popup(self):
        popup = SelectMethod(self)
        if self.folder_path:
            popup.set_folder_path(self.folder_path)
        popup.exec_()
