import os
import shutil
import webbrowser

from PyQt5.QtGui import QColor, QFont, QIcon
from PyQt5.QtWidgets import (QDialog, QMainWindow, QMessageBox, QPushButton,
                             QVBoxLayout, QWidget)
from view.ButtonPanel import ButtonPanel
from view.CloseConfirmationDialog import CloseConfirmationDialog
from view.FolderList import FolderList
from view.FrameSettings import FrameSettings
from view.HistoryManager import HistoryManager
from view.ImageDisplay import ImageDisplay
from view.InformationDialog import \
    InformationDialog  # Import InformationDialog
from view.SelectMethod import SelectMethod


class MainWindow(QMainWindow):
    def __init__(self, initial_folder):
        super().__init__()
        self.setWindowTitle("VisionAI")
        self.setGeometry(100, 100, 1200, 800)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.frame_settings = FrameSettings(self.central_widget, color=QColor(30, 30, 30))
        self.layout.addLayout(self.frame_settings.layout)

        self.history_manager = HistoryManager(self)
        self.image_display = ImageDisplay(self)

        self.folder_list = FolderList(self)  # Instantiate FolderList widget
        self.button_panel = ButtonPanel(self)

        self.layout.addWidget(self.folder_list)  # Add FolderList widget to layout
        self.layout.addWidget(self.image_display)

        self.showMaximized()
        
        self.initial_directory = initial_folder  # Store the initial directory
        self.history_manager.load_initial_directory(self.initial_directory)

        # Set the default font for all widgets in the main window
        self.set_font_for_all_widgets(self, "Consolas", 12)

    def set_font_for_all_widgets(self, widget, font_family, font_size):
        font = QFont(font_family, font_size)
        widget.setFont(font)
        for child in widget.children():
            if isinstance(child, QWidget):
                self.set_font_for_all_widgets(child, font_family, font_size)

    def update_view(self, folder_path):
        self.history_manager.update_history(folder_path)
        self.image_display.display_folder_contents(folder_path)
        self.folder_list.load_folders_and_images(folder_path)
        self.update_path_label(folder_path)
        self.update_image_count_label(folder_path)

    def update_path_label(self, path):
        self.button_panel.update_path_label(path)

    def update_image_count_label(self, folder_path):
        self.button_panel.update_image_count_label(folder_path)

    def open_select_method(self):
        popup = SelectMethod(self)  # Updated class name
        popup.exec_()
        
    def confirm_delete(self):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete the album folder?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            folder_path = self.folder_list.selected_folder_path
            if folder_path:
                try:
                    shutil.rmtree(folder_path)
                    QMessageBox.information(self, 'Success', 'Folder deleted successfully!')
                    # Optionally, you can update the view after deletion
                    self.folder_list.load_folders_and_images(self.initial_directory)
                except Exception as e:
                    QMessageBox.warning(self, 'Error', f'An error occurred while deleting the folder: {str(e)}')
        else:
            return

    def open_demo(self):
        webbrowser.open("https://huggingface.co/spaces/jagruthh/cities_small")

    def show_information(self):
        info_dialog = InformationDialog(self)
        info_dialog.exec_()

    def closeEvent(self, event):
        dialog = CloseConfirmationDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            event.accept()
        else:
            event.ignore()
