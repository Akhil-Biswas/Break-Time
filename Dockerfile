# Use official Python image
FROM python:3.12-slim

# Working directory
WORKDIR /Break-Time

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install mypy for static type checking during GitHub Actions/CI tests
RUN pip install --no-cache-dir mypy

# Copy project files
COPY . .

# Expose application port
EXPOSE 5000

# Start application
CMD ["python", "app/app.py"]