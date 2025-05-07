#!/bin/sh

# Exit on error
set -e
#setup package installer
pip install -r requirements.txt

echo "Making database migrations..."
python manage.py makemigrations

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

