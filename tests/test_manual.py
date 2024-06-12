import os
import sys
from pathlib import Path

import pytest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton
from pytestqt import qtbot

# Add the project root to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.Manual import Manual


def test_handle_new_album_creation_existing_file(qtbot, tmpdir):
    initial_directory = Path(tmpdir.mkdir("images"))
    
    image_paths = [initial_directory / "image1.jpg", initial_directory / "image2.png"]
    for image_path in image_paths:
        image_path.write_text("dummy data", encoding='utf-8')
    
    album_name = "New Album"
    album_path = initial_directory / album_name
    album_path.mkdir()
    existing_file_path = album_path / "image1.jpg"
    existing_file_path.write_text("existing file", encoding='utf-8')

    parent = QDialog()
    parent.update_view = lambda x: None  # Mock the update_view method
    album_dialog = QDialog()

    qtbot.addWidget(parent)
    qtbot.addWidget(album_dialog)

    album_input = QLineEdit(album_dialog)
    album_input.setText(album_name)

    manual_instance = Manual(parent, str(initial_directory))

    manual_instance.handle_new_album_creation(album_input, [str(p) for p in image_paths], album_dialog)

    assert existing_file_path.read_text(encoding='utf-8') == "existing file"
    
    new_file_path = album_path / "image2.png"
    assert new_file_path.exists()

    qtbot.mouseClick(album_dialog.findChild(QPushButton, "Create"), Qt.LeftButton)

if __name__ == '__main__':
    pytest.main(["-v", __file__])
