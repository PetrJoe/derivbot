#!/bin/sh

# Exit on error
set -e
#setup package installer
pip install -r requirements.txt --no-cache-dir

echo "Making database migrations..."
python manage.py makemigrations

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput


# Clean up unnecessary files to reduce size
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete
find . -type d -name "tests" -exec rm -rf {} +
find . -type d -name "test" -exec rm -rf {} +

gunicorn --config run.py deriv.wsgi:application
