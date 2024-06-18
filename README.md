# VisionAI

![VisionAI Logo](https://i.ibb.co/sq5J35B/Screenshot-2024-06-12-094922.png)

VisionAI is a PyQt5-based desktop application for organizing image collections using Vision AI and manual tools. Users can select folders, navigate history, sort folders, view individual images, open subfolders, and delete unwanted folders. VisionAI leverages AI to analyze and categorize images, enhancing the manual organization process and making it efficient to manage large image collections.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Datasets](#datasets)
- [Project Structure](#project-structure)
- [Demo](#demo)
- [Burndown Chart](#burndown-chart)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Select Folder:** Choose a directory to display its contents.
- **Navigate History:** Use back and forward buttons to navigate through folder history.
- **Sort Folders:** Sort folders by the number of images they contain.
- **View Images:** Double-click to view single images.
- **Open Folder:** Double-click to open any displayed folder.
- **Vision AI:** Automatically create albums for folders using Vision AI.
- **Manual Classification:** Manually create albums for selected images.
- **Web Demo:** View a web demo hosted on Hugging Face.
- **Rename Folder:** Rename an album folder with confirmation.
- **Delete Folder:** Delete an album folder with confirmation.
- **Information Dialog:** View instructions and information about the application.

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/mmgallai/VisionAI.git
   cd VisionAI
   ```

2. **Create and activate a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Install PyQt5:**
   ```
   pip install PyQt5
   ```

5. **Install pytest and pytest-qt for testing:**
   ```
   pip install pytest pytest-qt
   ```

## Usage

1. **Run the application:**
   ```
   python app.py
   ```

2. **Interact with the UI:**
   - Use the buttons to navigate, sort, and select folders.
   - Double-click on images to view them.
   - Use the "Vision AI" and "Manual" buttons to organize images.
   - Use the "Delete" button to remove folders.

## Testing

1. **Run the tests:**
   ```
   pytest tests/
   ```

## Datasets
1. **Link to Dataset :** [Subset of parent](https://drive.google.com/drive/folders/1Drk4mrMexkMgB0lk4JvJPYrQYq1OvzFL)
2. **Link to Parent Dataset :** [Parent dataset](https://www.kaggle.com/datasets/amaralibey/gsv-cities/data)
   
## Project Structure

```
VisionAI/
├── controller/
│   ├── AI.py
│   └── Manual.py
├── view/
│   ├── ButtonPanel.py
│   ├── ButtonStyle.py
│   ├── CloseConfirmationDialog.py
│   ├── DemoButton.py
│   ├── FolderList.py
│   ├── FrameSettings.py
│   ├── HistoryManager.py
│   ├── ImageDisplay.py
│   ├── InformationDialog.py
│   ├── InitialFolderSelection.py
│   ├── MainView.py
│   ├── UploadButton.py
│   └── SelectMethod.py
├── tests/
│   ├── __init__.py
│   ├── test_AI_NumberOfOutputs.py
│   ├── test_AI_PredictedCity.py
│   ├── test_AI_Preprocessing.py
│   ├── test_ButtonPanel.py
│   ├── test_Delete_FolderList.py
│   ├── test_IconsExist.py
│   ├── test_ImageCount.py
│   ├── test_InformationDialog.py
│   ├── test_Manual.py
│   ├── test_ModelExist.py
│   ├── test_SelectMethod.py
│   └── test_WebDemo.py
├── test images/
│   ├── image1.jpg
│   ├── image2.jpg
│   ├── image3.jpg
│   ├── image4.jpg
│   ├── image5.jpg
│   ├── image6.jpg
│   ├── image7.jpg
│   ├── image8.jpg
│   ├── image9.jpg
│   ├── image10.jpg
│   └── names.txt
├── icons/
│   ├── back_icon.png
│   ├── delete_icon.png
│   ├── directories_icon.png
│   ├── folder_icon.png
│   ├── forward_icon.png
│   ├── image_icon.png
│   ├── info_icon.png
│   ├── method_icon.png
│   └── sort_icon.png
├── model/
│   └── best.onnx
├── app.py
├── requirements.txt
└── README.md

```
- app.py: The main entry point for the application.

## Demo
![Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHAydWU3MnE5dnZ4Njg4eXdzYnBkZDgwMzJnemw0Z3Z0azl1MmN0MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Y5rMvrTf8JABxYHAPh/giphy.gif)

## Burndown Chart
![Burndown Chart](https://i.ibb.co/9TLgm7g/Sprint-burndown.png)

## Technologies Used
- <img src="https://img.icons8.com/color/48/000000/python.png" alt="Python" width="48" height="48"> **Python**: The primary programming language used for this project.
- <img src="https://upload.wikimedia.org/wikipedia/commons/e/e6/Python_and_Qt.svg" alt="PyQt5" width="48" height="48"> **PyQt5**: Used for creating the graphical user interface.
- <img src="https://upload.wikimedia.org/wikipedia/commons/1/17/Open_Neural_Network_Exchange_logo.svg" alt="ONNX" width="48" height="48"> **ONNX**: Used for the machine learning models.
- <img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg" alt="pytest" width="48" height="48"> **pytest**: Used for testing the application.
- <img src="https://img.icons8.com/fluent/48/000000/github.png" alt="GitHub" width="48" height="48"> **GitHub**: For version control and collaboration.


## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgements

- This project uses PyQt5 for the graphical user interface.
- This project uses [YOLOv8](https://github.com/ultralytics/ultralytics) to organize images.
- Special thanks to user "[amaralibey](https://www.kaggle.com/amaralibey)" in kaggle for the datatset.
- Special thanks to the contributors and the open-source community for their support.

