import unittest
from PyQt5.QtWidgets import QApplication, QToolButton
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from view.MainView import MainWindow

class TestButtonPanel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
    
    def setUp(self):
        self.window = MainWindow(initial_folder=".")
        self.button_panel = self.window.button_panel
    
    def test_ButtonPanelExists(self):
        buttons = self.find_buttons_in_layout(self.button_panel.layout)
        self.assertEqual(len(buttons), 8, "There should be exactly 8 buttons in the button panel")
    
    def find_buttons_in_layout(self, layout):
        buttons = []
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget = item.widget()
            if isinstance(widget, QToolButton):
                buttons.append(widget)
            elif widget is not None and widget.layout() is not None:
                buttons.extend(self.find_buttons_in_layout(widget.layout()))
        return buttons

if __name__ == '__main__':
    unittest.main()