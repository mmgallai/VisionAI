import os
import shutil

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QFileDialog, QListWidget, QListWidgetItem,
                             QMessageBox)


class FolderList(QListWidget):
    def __init__(self, parent):
        super().__init__(parent.central_widget)
        self.parent = parent
        self.setStyleSheet("background-color: #2b2b2b; color: white;")
        self.parent.frame_settings.layout.addWidget(self, 1, 0)
        self.itemClicked.connect(self.on_folder_selected)
        self.selected_folder_path = None  # Initialize selected_folder_path attribute

    def load_folders_and_images(self, directory, sort=False):
        self.clear()
        folders = []
        images = []
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                image_count = len([f for f in os.listdir(item_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))])
                folders.append((item, image_count, item_path))
            elif os.path.isfile(item_path) and item.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                images.append(item_path)
        if sort:
            folders.sort(key=lambda x: x[1])
        for folder_name, image_count, folder_path in folders:
            list_item = QListWidgetItem(f"{folder_name} ({image_count} images)")
            list_item.setIcon(QIcon("icons/folder_icon.png"))
            list_item.setData(Qt.UserRole, folder_path)
            self.addItem(list_item)
        for image_path in images:
            image_name = os.path.basename(image_path)
            list_item = QListWidgetItem(image_name)
            list_item.setIcon(QIcon("icons/image_icon.png"))
            list_item.setData(Qt.UserRole, image_path)
            self.addItem(list_item)

    def on_folder_selected(self, item):
        item_path = item.data(Qt.UserRole)
        if os.path.isdir(item_path):
            self.selected_folder_path = item_path  # Update selected_folder_path
            self.delete_folder(item_path)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self.parent, "Select Folder")
        if folder_path:
            self.selected_folder_path = folder_path  # Update selected_folder_path
            self.parent.history_manager.update_history(folder_path)
            self.parent.image_display.display_folder_contents(folder_path)
            self.load_folders_and_images(folder_path)
            self.parent.update_path_label(folder_path)
            self.parent.update_image_count_label(folder_path)

    def delete_folder(self, folder_path):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete the album folder?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if folder_path:
                try:
                    shutil.rmtree(folder_path)
                    QMessageBox.information(self, 'Success', 'Folder deleted successfully!')
                    # Optionally, you can update the view after deletion
                    self.load_folders_and_images(os.path.dirname(folder_path))
                except Exception as e:
                    QMessageBox.warning(self, 'Error', f'An error occurred while deleting the folder: {str(e)}')
        else:
            return

    def sort_albums(self):
        current_directory = self.parent.history_manager.current_directory()
        self.load_folders_and_images(current_directory, sort=True)
