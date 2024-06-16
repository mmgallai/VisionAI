import sys
from PyQt5.QtWidgets import QApplication, QDialog
from view.MainView import MainWindow
from view.InitialFolderSelection import InitialFolderSelection

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    initial_folder_dialog = InitialFolderSelection()
    if initial_folder_dialog.exec_() == QDialog.Accepted:
        selected_folder = initial_folder_dialog.selected_folder
        window = MainWindow(initial_folder=selected_folder)
        window.show() 
        sys.exit(app.exec_())
    else:
        sys.exit(0)
