# Use official Python image
FROM python:3.12-slim

# Working directory
WORKDIR /Break-Time

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose application port
EXPOSE 5000

# Start application
CMD ["python", "app/app.py"]