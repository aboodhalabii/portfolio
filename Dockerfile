# Use an official Python runtime
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port (change if your app runs on another port)
EXPOSE 5000

# Run the Flask app (update app name if needed)
CMD ["python", "app.py"]
