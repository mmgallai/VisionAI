import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QStyle
from PyQt5.QtCore import Qt
from view.FrameSettings import FrameSettings
from view.IconButton import IconButton
from view.UploadButton import UploadButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Frame")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        self.frame_settings = FrameSettings(self.central_widget)
        self.layout.addLayout(self.frame_settings.layout)
        
        self.create_icon_button()
        self.create_upload_button()
        self.showMaximized()

    def create_icon_button(self):
        label_text = "Name of the album\nNumber of photos"
        button_size = (128, 128)
        icon_size = (100, 100)
        button = IconButton(QStyle.SP_DirIcon, label_text, button_size, icon_size, self.central_widget)
        self.frame_settings.layout.addWidget(button, 0, 0, alignment=Qt.AlignTop | Qt.AlignLeft)

    def create_upload_button(self):
        upload_button = UploadButton(self.central_widget)
        self.frame_settings.layout.addWidget(upload_button, 1, 0, alignment=Qt.AlignBottom | Qt.AlignLeft)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
