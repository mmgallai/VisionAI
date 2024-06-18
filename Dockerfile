# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Temporarily disable APT post-invoke hooks to avoid errors
RUN mv /var/lib/dpkg/info /var/lib/dpkg/info.bak && mkdir /var/lib/dpkg/info

# Update the apt package list and install necessary libraries for PyQt5 and OpenGL in one RUN command
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxkbcommon-x11-0 \
    libx11-xcb1 \
    libxcb-glx0 \
    libxcb-keysyms1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Restore APT post-invoke hooks
RUN rm -rf /var/lib/dpkg/info && mv /var/lib/dpkg/info.bak /var/lib/dpkg/info

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
