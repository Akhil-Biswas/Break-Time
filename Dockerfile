# Use official Python image
FROM python:3.12-slim

# Working directory
WORKDIR /Break-Time

# Install uv
RUN pip install --no-cache-dir uv

# Copy dependency files first
COPY pyproject.toml uv.lock ./

# Install project dependencies and tests (GitHub Actions/CI)
RUN uv sync --frozen \
        --group test

# Copy project files
COPY . .

# Expose application port
EXPOSE 5000

# Start the application
CMD ["uv", "run", "python", "app/app.py"]