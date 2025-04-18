# Use an official Python image with GUI support (use slim if GUI is not needed)
FROM python:3.11-slim

# Install dependencies needed for GUI and testing
RUN apt-get update && \
    apt-get install -y python3-tk xvfb && \
    rm -rf /var/lib/apt/lists/*

# Set working directory in container
WORKDIR /app

# Copy all files to the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run tests
RUN pytest test_cafe_logic.py

# Optional: default command to run the GUI app using virtual display
CMD ["xvfb-run", "-a", "python", "main.py"]
