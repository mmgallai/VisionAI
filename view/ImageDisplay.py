from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class ImageDisplay(QScrollArea):
    def __init__(self, parent):
        super().__init__(parent.central_widget)
        self.parent = parent
        self.setWidgetResizable(True)

    def display_single_image(self, image_path):
        self.clear_layout()
        scroll_widget = QWidget()
        scroll_layout = QGridLayout(scroll_widget)
        pixmap = QPixmap(image_path).scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        scroll_layout.addWidget(label, 0, 0, 1, 4)  # Single image takes the entire row
        self.setWidget(scroll_widget)
        self.parent.frame_settings.layout.addWidget(self, 2, 0)

    def display_folder_contents(self, folder_path):
        self.clear_layout()
        scroll_widget = QWidget()
        scroll_layout = QGridLayout(scroll_widget)
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        row = 0
        col = 0
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            pixmap = QPixmap(image_path).scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            label = QLabel()
            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignCenter)
            scroll_layout.addWidget(label, row, col)
            col += 1
            if col == 4:  # Move to the next row after 3 images
                col = 0
                row += 1
        self.setWidget(scroll_widget)
        self.parent.frame_settings.layout.addWidget(self, 2, 0)
        self.parent.update_image_count_label(folder_path)

    def clear_layout(self):
        while self.parent.frame_settings.layout.count() > 2:
            item = self.parent.frame_settings.layout.takeAt(2)
            if item.widget():
                item.widget().deleteLater()
