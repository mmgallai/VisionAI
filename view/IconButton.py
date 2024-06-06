from PyQt5.QtWidgets import QPushButton, QApplication, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize

class IconButton(QWidget):
    def __init__(self, icon_type, text, button_size=(128, 128), icon_size=(64, 64), parent=None):
        super().__init__(parent)
        self.button = QPushButton(self)
        icon = QApplication.style().standardIcon(icon_type)
        self.button.setIcon(icon)
        self.button.setIconSize(QSize(*icon_size))
        self.button.setFlat(True)
        self.button.setFixedSize(*button_size)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("color: white;")
        self.label.adjustSize()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.button.setCursor(Qt.PointingHandCursor)

    def enterEvent(self, event):
        self.button.setCursor(Qt.PointingHandCursor)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.button.setCursor(Qt.ArrowCursor)
        super().leaveEvent(event)
