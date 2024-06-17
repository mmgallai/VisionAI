# Use the official Python image from Docker Hub as the base image
FROM python:3.9-slim

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
    libxcb-image0 \
    libxcb-shm0 \
    libxcb-icccm4 \
    libxcb-sync1 \
    libxcb-xfixes0 \
    libxcb-shape0 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-xinerama0 \
    libxcb-util1 \
    libxrender1 \
    libxi6 \
    libsm6 \
    libfontconfig1 \
    libfreetype6 \
    libxext6 \
    libx11-6 \
    libxau6 \
    libxdmcp6 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxrandr2 \
    libxinerama1 \
    libxfixes3 \
    libxtst6 \
    libxss1 \
    libxxf86vm1 \
    libdbus-1-3 \
    libxcb-render0 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libpango-1.0-0 \
    libgdk-pixbuf2.0-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory contents into the container
COPY . .

# Set environment variables for Qt to use offscreen platform
ENV QT_QPA_PLATFORM offscreen
ENV XDG_RUNTIME_DIR /tmp/runtime-root

# Create the runtime directory
RUN mkdir -p /tmp/runtime-root && chmod 700 /tmp/runtime-root

# Specify the command to run the application
CMD ["python", "./app.py"]
