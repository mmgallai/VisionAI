from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QColor, QFont
from view.FrameSettings import FrameSettings
from view.ButtonPanel import ButtonPanel
from view.FolderList import FolderList
from view.ImageDisplay import ImageDisplay
from view.HistoryManager import HistoryManager
from view.SelectMethod import SelectMethod
from view.CloseConfirmationDialog import CloseConfirmationDialog
import os
import webbrowser

class MainWindow(QMainWindow):
    def __init__(self, initial_folder):
        super().__init__()
        self.setWindowTitle("VisonAI")
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
        QMessageBox.information(self, "Information", 
            "This software allows you to organize images using Vision AI or manually.\n"
            "Features include:\n"
            "1. Selecting a folder to display its contents.\n"
            "2. Navigation through history with back and forward buttons.\n"
            "3. Sorting folders by the number of images they contain.\n"
            "4. Viewing single images on double-click.\n"
            "5. Clicking 'Vision AI' will create albums for their respective folders.\n"
            "6. Selecting 'Manual' will allow you to selectively create albums for particular images, including the option to select multiple images.\n"
            "\n"
            "Instructions:\n"
            "1. Select 'Select Folder' to choose a directory.\n"
            "2. Use 'Select Method' to choose Vision AI or Manual classification.\n"
            "3. Navigate through folders using 'Back' and 'Forward' buttons.\n"
            "4. View web demo to check model performance and working, hosted on Hugging Face.\n"
            "5. The number of images in the current folder is displayed at the bottom right corner.\n"
            "6. The current directory path is displayed at the bottom right corner, just above the number of images.\n"
        )


    def closeEvent(self, event):
        dialog = CloseConfirmationDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            event.accept()
        else:
            event.ignore()
