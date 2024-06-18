# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Disable the progress bar to avoid threading issues
ENV PIP_NO_PROGRESS_BAR=off

# Upgrade pip to a stable version separately
RUN python -m pip install --upgrade pip==24.0

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
