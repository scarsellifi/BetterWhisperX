# Use a base image of Python 3.11
FROM python:3.11-slim

# Install ffmpeg version 4 and other system dependencies
RUN apt-get update && apt-get install -y ffmpeg

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make the test script executable
RUN chmod +x test_script.sh

# Command to run a test script
CMD ["bash", "test_script.sh"]
