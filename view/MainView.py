import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QToolButton, QListWidget, QListWidgetItem, QLabel, QScrollArea, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QColor, QPalette, QPixmap
from view.FrameSettings import FrameSettings
from view.PopUpWindow import PopUpWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Frame")
        self.setGeometry(100, 100, 1200, 800)  # Set a larger default size for the main window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        self.frame_settings = FrameSettings(self.central_widget, color=QColor(30, 30, 30))
        self.layout.addLayout(self.frame_settings.layout)
        
        self.history = []
        self.history_index = -1
        
        self.create_buttons()
        self.create_folder_list()
        self.create_path_label()
        self.create_image_count_label()
        self.showMaximized()

        self.load_initial_directory(os.getcwd())

    def create_buttons(self):
        self.button_layout = QHBoxLayout()

        self.back_button = self.create_icon_button("Back", "back_icon.png", self.go_back)
        self.button_layout.addWidget(self.back_button)

        self.forward_button = self.create_icon_button("Forward", "forward_icon.png", self.go_forward)
        self.button_layout.addWidget(self.forward_button)

        select_folder_button = self.create_icon_button("Select Folder", "directories_icon.png", self.select_folder)
        self.button_layout.addWidget(select_folder_button)

        select_method_button = self.create_icon_button("Select Method", "method_icon.png", self.open_select_method)
        self.button_layout.addWidget(select_method_button)

        demo_button = self.create_icon_button("Web Demo", "demo_icon.png", self.open_demo)
        self.button_layout.addWidget(demo_button)

        info_button = self.create_icon_button("Information", "info_icon.png", self.show_information)
        self.button_layout.addWidget(info_button)

        self.button_layout.addStretch()
        self.frame_settings.layout.addLayout(self.button_layout, 0, 0, alignment=Qt.AlignTop | Qt.AlignLeft)

        self.update_navigation_buttons()

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

        self.folder_list.itemDoubleClicked.connect(self.on_folder_selected)

    def create_path_label(self):
        self.path_label = QLabel(self)
        self.path_label.setAlignment(Qt.AlignRight)
        self.path_label.setStyleSheet("color: white; font-size: 16px;")
        self.layout.addWidget(self.path_label)
        self.layout.setAlignment(self.path_label, Qt.AlignRight)

    def create_image_count_label(self):
        self.image_count_label = QLabel(self)
        self.image_count_label.setAlignment(Qt.AlignRight)
        self.image_count_label.setStyleSheet("color: white; font-size: 16px;")
        self.layout.addWidget(self.image_count_label)
        self.layout.setAlignment(self.image_count_label, Qt.AlignRight)

    def load_initial_directory(self, directory):
        self.update_history(directory)
        self.load_folders_and_images(directory)
        self.display_folder_contents(directory)
        self.update_path_label(directory)

    def load_folders_and_images(self, directory):
        self.folder_list.clear()
        items = [f for f in os.listdir(directory)]
        
        for item in items:
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                list_item = QListWidgetItem(item)
                list_item.setIcon(QIcon("folder_icon.png"))  # Replace with path to your folder icon
                list_item.setData(Qt.UserRole, item_path)
            elif os.path.isfile(item_path) and item.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                list_item = QListWidgetItem(item)
                list_item.setIcon(QIcon("image_icon.png"))  # Replace with path to your image icon
                list_item.setData(Qt.UserRole, item_path)
            else:
                continue

            self.folder_list.addItem(list_item)

    def on_folder_selected(self, item):
        item_path = item.data(Qt.UserRole)
        if os.path.isdir(item_path):
            self.update_history(item_path)
            self.display_folder_contents(item_path)
            self.load_folders_and_images(item_path)
            self.update_path_label(item_path)
            self.update_image_count_label(item_path)
        else:
            # Display the image in the lower view
            self.display_single_image(item_path)

    def display_single_image(self, image_path):
        # Remove all widgets below the button layout but keep the buttons and path label
        while self.frame_settings.layout.count() > 2:  # Keep the button layout and folder list
            item = self.frame_settings.layout.takeAt(2)
            if item.widget():
                item.widget().deleteLater()

        # Display single image
        scroll_area = QScrollArea(self.central_widget)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        
        pixmap = QPixmap(image_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        scroll_layout.addWidget(label)
        
        scroll_area.setWidget(scroll_widget)
        self.frame_settings.layout.addWidget(scroll_area, 2, 0)

    def display_folder_contents(self, folder_path):
        # Remove all widgets below the button layout but keep the buttons and path label
        while self.frame_settings.layout.count() > 2:  # Keep the button layout and folder list
            item = self.frame_settings.layout.takeAt(2)
            if item.widget():
                item.widget().deleteLater()

        # Scroll area to display images
        scroll_area = QScrollArea(self.central_widget)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        
        if image_files:
            for image_file in image_files:
                image_path = os.path.join(folder_path, image_file)
                pixmap = QPixmap(image_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                label = QLabel()
                label.setPixmap(pixmap)
                label.setAlignment(Qt.AlignCenter)
                scroll_layout.addWidget(label)
        
        scroll_area.setWidget(scroll_widget)
        self.frame_settings.layout.addWidget(scroll_area, 2, 0)
        self.update_image_count_label(folder_path)  # Update image count label when displaying folder contents

    def update_history(self, folder_path):
        # Trim forward history if we're not at the latest entry
        if self.history_index < len(self.history) - 1:
            self.history = self.history[:self.history_index + 1]
        self.history.append(folder_path)
        self.history_index += 1
        self.update_navigation_buttons()

    def go_back(self):
        if self.history_index > 0:
            self.history_index -= 1
            folder_path = self.history[self.history_index]
            self.display_folder_contents(folder_path)
            self.load_folders_and_images(folder_path)
            self.update_navigation_buttons()
            self.update_path_label(folder_path)
            self.update_image_count_label(folder_path)

    def go_forward(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            folder_path = self.history[self.history_index]
            self.display_folder_contents(folder_path)
            self.load_folders_and_images(folder_path)
            self.update_navigation_buttons()
            self.update_path_label(folder_path)
            self.update_image_count_label(folder_path)

    def update_navigation_buttons(self):
        self.back_button.setEnabled(self.history_index > 0)
        self.forward_button.setEnabled(self.history_index < len(self.history) - 1)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.update_history(folder_path)
            self.display_folder_contents(folder_path)
            self.load_folders_and_images(folder_path)
            self.update_path_label(folder_path)
            self.update_image_count_label(folder_path)

    def open_select_method(self):
        popup = PopUpWindow(self)
        popup.exec_()

    def open_demo(self):
        import webbrowser
        webbrowser.open("https://huggingface.co/spaces/jagruthh/cities_small")

    def show_information(self):
        QMessageBox.information(self, "Information", 
            "This software allows you to organize images using Vision AI or manually.\n"
            "Instructions:\n"
            "1. Select 'Select Folder' to choose a directory.\n"
            "2. Use 'Select Method' to choose Vision AI or Manual classification.\n"
            "3. Navigate through folders using 'Back' and 'Forward' buttons.\n"
            "4. View web demo for additional details.\n"
            "5. The number of images in the current folder is displayed at the bottom right corner."
        )

    def update_view(self, folder_path):
        self.update_history(folder_path)
        self.display_folder_contents(folder_path)
        self.load_folders_and_images(folder_path)
        self.update_path_label(folder_path)
        self.update_image_count_label(folder_path)

    def update_path_label(self, path):
        self.path_label.setText(f"Current Path: {path}")

    def update_image_count_label(self, folder_path):
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        self.image_count_label.setText(f"Number of Images: {len(image_files)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
