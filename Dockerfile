# Use a specific version of Miniconda as the base image
FROM continuumio/miniconda3:4.9.2

# Set the working directory in the container
WORKDIR /app

# Update repository information and install necessary system libraries and Xvfb
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y --no-install-recommends apt-utils && \
    sed -i 's|http://deb.debian.org/debian buster|http://deb.debian.org/debian oldoldstable|g' /etc/apt/sources.list && \
    sed -i 's|http://security.debian.org/debian-security buster/updates|http://security.debian.org/debian-security oldoldstable/updates|g' /etc/apt/sources.list && \
    apt-get update --allow-releaseinfo-change && \
    apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxkbcommon-x11-0 \
    libxcb-glx0 \
    libxcb-keysyms1 \
    libx11-xcb1 \
    libxrender1 \
    libfontconfig1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxtst6 \
    libxi6 \
    libxrandr2 \
    libxss1 \
    libxshmfence1 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-shm0 \
    libxcb-util0 \
    libxcb-xfixes0 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-xinerama0 \
    xvfb && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables for Qt
ENV QT_XCB_GL_INTEGRATION=none
ENV QT_DEBUG_PLUGINS=1

# Copy the environment configuration file
COPY environment.yml .

# Create the Conda environment specified in environment.yml
RUN conda env create -f environment.yml

# Install onnxruntime via pip
RUN conda run -n myenv pip install onnxruntime==1.8.0

# Make sure the environment is activated by default
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# Copy the rest of the application code into the container
COPY . .

# Define environment variable
ENV NAME World

# Start Xvfb and run the application when the container launches
CMD ["bash", "-c", "xvfb-run -a python app.py"]
