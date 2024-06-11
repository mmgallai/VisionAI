from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget
from view.ButtonStyle import ButtonStyle  # Import ButtonStyle
from view.SelectMethod import SelectMethod


class UploadButton(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.folder_path = None
        self.button = QPushButton("Select Method", self)
        self.button.clicked.connect(self.show_popup)
        self.button.setStyleSheet(ButtonStyle.get_large_style())  # Use ButtonStyle

        #Adding a Delete Button
        self.delete_button = QPushButton("Delete Album", self)
        self.delete_button.clicked.connect(self.confirm_delete)
        self.delete_button.setStyleSheet(ButtonStyle.get_large_style())

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.delete_button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
        
    def setFolderPath(self, folder_path):
        self.folder_path = folder_path

    def show_popup(self):
        popup = SelectMethod(self)
        if self.folder_path:
            popup.set_folder_path(self.folder_path)
        popup.exec_()


    # Showing Confirmation Dialog for Deletion
    def confirm_delete(self):
        if not self.folder_path:
            QMessageBox.warning(self, "Delete Album", "No album folder selected.")
            return

        confirm_dialog = QMessageBox.question(self, "Delete Album", "Are you sure you want to delete the album folder?", 
                                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm_dialog == QMessageBox.Yes:
            # Perform deletion operation here
            QMessageBox.information(self, "Delete Album", "Album folder deleted successfully.")
            # Optionally emit a signal or perform any further actions after deletion
