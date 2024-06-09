from PyQt5.QtWidgets import QHBoxLayout, QToolButton, QWidget, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import os  # Add this import

class ButtonPanel:
    def __init__(self, parent):
        self.parent = parent
        self.layout = QHBoxLayout()
        self.path_label = QLabel(self.parent)  # Initialize path label
        self.image_count_label = QLabel(self.parent)  # Initialize image count label
        self.create_buttons()
        
        self.layout.addWidget(self.path_label)  # Add path label to layout
        self.layout.addWidget(self.image_count_label)  # Add image count label to layout

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
                padding: 10px;
            }
            QToolButton:hover {
                background-color: #3EB489;
            }
            """
        )
        button.clicked.connect(callback)
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: white; font-size: 12px;")
        button_layout.addWidget(button)
        button_layout.addWidget(label)
        button_layout.setAlignment(Qt.AlignCenter)
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
        self.image_count_label.setStyleSheet("color: white")

    def show_close_confirmation(self):
        reply = QMessageBox.question(self.parent, 'Close Confirmation', 'Are you sure you want to close the application?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        return reply == QMessageBox.Yes
