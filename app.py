import sys
from PyQt5.QtWidgets import QApplication, QDialog
from view.MainView import MainWindow
from view.InitialFolderSelection import InitialFolderSelection

if __name__ == "__main__":
    print("Starting application...")
    app = QApplication(sys.argv)
    
    
    print("Showing initial folder selection dialog...")
    initial_folder_dialog = InitialFolderSelection()
    if initial_folder_dialog.exec_() == QDialog.Accepted:
        print("Dialog accepted")
        selected_folder = initial_folder_dialog.selected_folder
        window = MainWindow(initial_folder=selected_folder)
        window.show()
        print("Showing Main Window...")
        sys.exit(app.exec_())
    else:
        print("Dialog canceled")
        sys.exit(0)
