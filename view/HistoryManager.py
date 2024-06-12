class HistoryManager:
    def __init__(self, parent):
        self.parent = parent
        self.history = []
        self.history_index = -1

    def load_initial_directory(self, directory):
        self.update_history(directory)
        self.parent.image_display.display_folder_contents(directory)
        self.parent.folder_list.load_folders_and_images(directory)
        self.parent.update_path_label(directory)

    def update_history(self, folder_path):
        if self.history_index < len(self.history) - 1:
            self.history = self.history[:self.history_index + 1]
        self.history.append(folder_path)
        self.history_index += 1
        self.update_navigation_buttons()

    def go_back(self):
        if self.history_index > 0:
            self.history_index -= 1
            folder_path = self.history[self.history_index]
            self.parent.image_display.display_folder_contents(folder_path)
            self.parent.folder_list.load_folders_and_images(folder_path)
            self.parent.update_path_label(folder_path)
            self.parent.update_image_count_label(folder_path)
            self.update_navigation_buttons()

    def go_forward(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            folder_path = self.history[self.history_index]
            self.parent.image_display.display_folder_contents(folder_path)
            self.parent.folder_list.load_folders_and_images(folder_path)
            self.parent.update_path_label(folder_path)
            self.parent.update_image_count_label(folder_path)
            self.update_navigation_buttons()

    def update_navigation_buttons(self):
        can_go_back = self.history_index > 0
        can_go_forward = self.history_index < len(self.history) - 1
        self.parent.button_panel.update_navigation_buttons(can_go_back, can_go_forward)

    def current_directory(self):
        return self.history[self.history_index] if self.history else os.getcwd()
