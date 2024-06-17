# Use the official Python image from Docker Hub as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install necessary libraries for PyQt5 and OpenGL
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxkbcommon-x11-0 \
    libx11-xcb1 \
    libxcb-glx0 \
    libxcb-keysyms1 \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Qt to use offscreen platform
ENV QT_QPA_PLATFORM=offscreen

# Create the runtime directory
ENV XDG_RUNTIME_DIR=/tmp/runtime-root
RUN mkdir -p /tmp/runtime-root && chmod 700 /tmp/runtime-root

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory contents into the container
COPY . .

# Specify the command to run the application
CMD ["python", "./app.py"]
