FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements-prod.txt .
RUN pip install --no-cache-dir -r requirements-prod.txt

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p static

# Expose port
EXPOSE 8000

# Run the application
CMD gunicorn deriv.wsgi:application
