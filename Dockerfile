# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the app.py directory
COPY app.py /app

# Copy requirements.txt (if it's outside "app.py/")
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.app

# Run the app.py
CMD ["python", "-m", "app"]