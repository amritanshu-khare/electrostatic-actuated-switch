# Use the official Python base image for Python 3.11.4
FROM python:3.11.4-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app files to the container
COPY . /app

# Install dependencies
RUN pip install flask numpy pandas matplotlib tensorflow

# Expose the port on which your Flask app runs (default is 5000)
EXPOSE $PORT

# Set the entry point to run the Flask app
CMD ["python", "app.py"]
