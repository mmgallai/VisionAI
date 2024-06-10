class ButtonStyle:
    @staticmethod
    def get_default_style():
        return """
        QPushButton {
            border: 2px solid #3EB489; 
            color: white;
            font-size: 20px;
            padding: 10px;
            border-radius: 10px;
            background-color: transparent;
            font-family: Consolas;
        }
        QPushButton:hover {
            background-color: #3EB489;
        }
        """
