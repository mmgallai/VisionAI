import os
import shutil

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QFileDialog, QListWidget, QListWidgetItem,
                             QMessageBox, QDialog, QInputDialog, QMenu)

from view.DeleteConfirmationDialog import DeleteConfirmationDialog
class FolderList(QListWidget):
    def __init__(self, parent):
        super().__init__(parent.central_widget)
        self.parent = parent
        self.setStyleSheet("background-color: #2b2b2b; color: white;")
        self.parent.frame_settings.layout.addWidget(self, 1, 0)
        self.itemDoubleClicked.connect(self.on_folder_double_clicked)
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

    def on_folder_double_clicked(self, item):
        item_path = item.data(Qt.UserRole)
        if os.path.isdir(item_path):
            self.selected_folder_path = item_path  # Update selected_folder_path
            self.parent.update_view(item_path)  # Call update_view on parent to show contents

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
        dialog = DeleteConfirmationDialog(self)
        if dialog.exec_() == QDialog.Accepted:
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

    def contextMenuEvent(self, event):
        # Get the item at the clicked position
        item = self.itemAt(event.pos())
        if item:
            context_menu = QMenu(self)
            rename_action = context_menu.addAction("Rename Folder")
            rename_action.triggered.connect(lambda: self.rename_folder(item))
            context_menu.exec_(event.globalPos())

    def rename_folder(self, item):
        folder_path = item.data(Qt.UserRole)
        if os.path.isdir(folder_path):
            new_name, ok = QInputDialog.getText(self, 'Rename Folder', 'Enter new folder name:')
            if ok and new_name:
                new_folder_path = os.path.join(os.path.dirname(folder_path), new_name)
                try:
                    os.rename(folder_path, new_folder_path)
                    QMessageBox.information(self, 'Success', 'Folder renamed successfully!')
                    
                    # Update the folder list to reflect the new name
                    self.load_folders_and_images(os.path.dirname(new_folder_path))
                except Exception as e:
                    QMessageBox.warning(self, 'Error', f'An error occurred while renaming the folder: {str(e)}')
        else:
            QMessageBox.warning(self, 'Error', 'Selected item is not a folder.')    

    