# Use the official Python image from Docker Hub as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory contents into the container
COPY . .

# Specify the command to run the application
CMD [ "python", "./app.py" ]
