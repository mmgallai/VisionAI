from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

class FrameSettings:
    def __init__(self, widget, color=Qt.black):
        self.widget = widget
        self.color = color
        self.setup_frame()

    def setup_frame(self):
        palette = self.widget.palette()
        palette.setColor(QPalette.Background, QColor(self.color))
        self.widget.setAutoFillBackground(True)
        self.widget.setPalette(palette)
        self.layout = QGridLayout()
        self.widget.setLayout(self.layout)
