# Use an official Python runtime
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy lightweight requirements
COPY requirements-light.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements-light.txt

# Copy the rest of the application
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the Flask app with gunicorn (production server)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
