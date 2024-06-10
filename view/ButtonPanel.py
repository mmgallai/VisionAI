from PyQt5.QtWidgets import QHBoxLayout, QToolButton, QWidget, QVBoxLayout, QLabel, QMessageBox, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
import os
from view.ButtonStyle import ButtonStyle  # Import ButtonStyle

class ButtonPanel:
    def __init__(self, parent):
        self.parent = parent
        self.layout = QHBoxLayout()
        self.path_label = QLabel(self.parent)
        self.image_count_label = QLabel(self.parent)
        self.create_buttons()
        
        self.layout.addWidget(self.path_label)
        self.layout.addWidget(self.image_count_label)

        self.parent.frame_settings.layout.addLayout(self.layout, 0, 0, alignment=Qt.AlignTop | Qt.AlignLeft)

    def create_buttons(self):
        self.back_button = self.add_button_with_label("Back", "icons/back_icon.png", self.parent.history_manager.go_back)
        self.forward_button = self.add_button_with_label("Forward", "icons/forward_icon.png", self.parent.history_manager.go_forward)
        self.add_button_with_label("Select Folder", "icons/directories_icon.png", self.parent.folder_list.select_folder)
        self.add_button_with_label("Select Method", "icons/method_icon.png", self.parent.open_select_method)
        self.add_button_with_label("Web Demo", "icons/demo_icon.png", self.parent.open_demo)
        self.add_button_with_label("Sort", "icons/sort_icon.png", self.parent.folder_list.sort_albums)
        self.add_button_with_label("Information", "icons/info_icon.png", self.parent.show_information)
        self.layout.addStretch()

    def add_button_with_label(self, text, icon_path, callback):
        button_widget = QWidget()
        button_layout = QVBoxLayout(button_widget)
        button = QToolButton(self.parent.central_widget)
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(48, 48))
        button.setToolTip(text)
        button.setStyleSheet(
            """
            QToolButton {
                border: none;
                background-color: transparent;
                padding: 0px;
                font-family: Consolas;
            }
            QToolButton:hover {
                background-color: #3EB489;
            }
            """
        )
        button.clicked.connect(callback)
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: white; font-family: Consolas; font-size: 16px;")  # Increased font size
        label.setFixedHeight(30)  # Ensure fixed height for better alignment

        button_layout.addWidget(button, alignment=Qt.AlignCenter)
        button_layout.addWidget(label, alignment=Qt.AlignCenter)
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setContentsMargins(33, 33, 0, 0)  # Remove margins

        button_widget.setLayout(button_layout)
        self.layout.addWidget(button_widget)
        return button

    def update_navigation_buttons(self, can_go_back, can_go_forward):
        self.back_button.setEnabled(can_go_back)
        self.forward_button.setEnabled(can_go_forward)

    def update_path_label(self, path):
        self.path_label.setText(f"")

    def update_image_count_label(self, folder_path):
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        self.image_count_label.setText(f"Number of Images: {len(image_files)}")
        font = QFont()
        font.setPointSize(18)
        font.setFamily("Consolas")
        self.image_count_label.setFont(font)
        self.image_count_label.setStyleSheet("color: white")

    def show_close_confirmation(self):
        reply = QMessageBox.question(self.parent, 'Close Confirmation', 'Are you sure you want to close the application?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        return reply == QMessageBox.Yes
