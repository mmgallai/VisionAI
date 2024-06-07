import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QToolButton, QListWidget, QListWidgetItem, QFileDialog
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QColor, QPalette
from view.FrameSettings import FrameSettings
from view.UploadButton import UploadButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Frame")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        self.frame_settings = FrameSettings(self.central_widget, color=QColor(30, 30, 30))
        self.layout.addLayout(self.frame_settings.layout)
        
        self.create_buttons()
        self.create_folder_list()
        self.showMaximized()

    def create_buttons(self):
        button_layout = QHBoxLayout()

        select_method_button = self.create_icon_button("Select Method", "method_icon.png", self.open_select_method)
        button_layout.addWidget(select_method_button)

        demo_button = self.create_icon_button("Demo", "demo_icon.png", self.open_demo)
        button_layout.addWidget(demo_button)

        button_layout.addStretch()
        self.frame_settings.layout.addLayout(button_layout, 0, 0, alignment=Qt.AlignTop | Qt.AlignLeft)

    def create_icon_button(self, tooltip, icon_path, callback):
        button = QToolButton(self.central_widget)
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(48, 48))  # Increased icon size
        button.setToolTip(tooltip)
        button.setStyleSheet(
            """
            QToolButton {
                border: none;
                background-color: transparent;
                padding: 10px;
            }
            QToolButton:hover {
                background-color: #3EB489; /* Mint color on hover */
            }
            """
        )
        button.clicked.connect(callback)
        return button

    def create_folder_list(self):
        self.folder_list = QListWidget(self.central_widget)
        self.folder_list.setStyleSheet("background-color: #2b2b2b; color: white;")
        self.frame_settings.layout.addWidget(self.folder_list, 1, 0)

        current_directory = os.getcwd()
        folders = [f for f in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, f))]
        
        for folder in folders:
            item = QListWidgetItem(folder)
            item.setIcon(QIcon("path_to_folder_icon.png"))  # Replace with path to your folder icon
            self.folder_list.addItem(item)

        self.folder_list.itemDoubleClicked.connect(self.on_folder_selected)

    def on_folder_selected(self, item):
        selected_folder = item.text()
        folder_path = os.path.join(os.getcwd(), selected_folder)
        self.open_select_method(folder_path)

    def open_select_method(self, folder_path=None):
        if not folder_path:
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        
        if folder_path:
            upload_button = UploadButton(self)
            upload_button.setFolderPath(folder_path)
            upload_button.show_popup()

    def open_demo(self):
        import webbrowser
        webbrowser.open("https://huggingface.co/spaces/jagruthh/cities_small")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
