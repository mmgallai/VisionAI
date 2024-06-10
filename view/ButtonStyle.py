class ButtonStyle:
    @staticmethod
    def get_default_style():
        return """
            QPushButton {
                border: 2px solid #3EB489; 
                color: white;
                font-size: 18px;
                border-radius: 15px;
                padding: 10px 20px;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: #3EB489;
            }
        """

    @staticmethod
    def get_large_style():
        return """
            QPushButton {
                border: 4px solid #3EB489; 
                color: white;
                font-family: 'shanti';
                font-size: 36px;
                border-radius: 25px;
                padding: 15px 30px; 
                background-color: transparent; 
            }
            QPushButton:hover {
                background-color: #3EB489; 
            }
        """
