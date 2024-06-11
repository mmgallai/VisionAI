from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDialog
from PyQt5.QtGui import QColor, QFont
from view.FrameSettings import FrameSettings
from view.ButtonPanel import ButtonPanel
from view.FolderList import FolderList
from view.ImageDisplay import ImageDisplay
from view.HistoryManager import HistoryManager
from view.SelectMethod import SelectMethod
from view.CloseConfirmationDialog import CloseConfirmationDialog
from view.InformationDialog import InformationDialog  # Import InformationDialog
import os
import webbrowser

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
        self.folder_list = FolderList(self)
        self.button_panel = ButtonPanel(self)

        self.layout.addWidget(self.folder_list)
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
        self.button_panel.update_navigation_buttons(
            self.history_manager.history_index > 0, 
            self.history_manager.history_index < len(self.history_manager.history) - 1
        )

    def update_path_label(self, path):
        self.button_panel.update_path_label(path)

    def update_image_count_label(self, folder_path):
        self.button_panel.update_image_count_label(folder_path)

    def open_select_method(self):
        popup = SelectMethod(self)  # Updated class name
        popup.exec_()

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
