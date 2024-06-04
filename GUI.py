import sys
import os
import warnings

# Ignore specific deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QListJsonWidget, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# Define the main class for the Photo Organizer application, inheriting from QMainWindow
class PhotoOrganizer(QMainWindow):
    # Initialize the main window
    def __init__(self):
        super().__init__()
        # Set up the user interface
        self.initUI()
        # Initialize a dictionary to store album data
        self.albums = {}
