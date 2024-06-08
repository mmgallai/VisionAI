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
        palette.setColor(QPalette.Window, QColor(self.color))
        self.widget.setAutoFillBackground(True)
        self.widget.setPalette(palette)
        
        # Check if the widget already has a layout
        if not self.widget.layout():
            self.layout = QGridLayout()
            self.widget.setLayout(self.layout)
        else:
            self.layout = self.widget.layout()
