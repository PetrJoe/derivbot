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

"""
#!/bin/bash

# Exit on error
set -e

echo "===== Deriv Trading Bot Setup and Run Script ====="

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv env
fi

# Activate virtual environment
echo "Activating virtual environment..."
source env/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
echo "Creating necessary directories..."
mkdir -p static
mkdir -p data

# Run migrations
echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "Creating sample .env file..."
    cat > .env << EOL
APP_ID=YOUR_DERIV_APP_ID
SYMBOL=R_75
GRANULARITY=300
CANDLE_COUNT=100
CSV_FILE=data/data.csv
CHART_FILE=chart.png
UPDATE_INTERVAL=300
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
DJANGO_SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')
EOL
    echo "Please edit the .env file with your actual credentials before running the bot."
    exit 1
fi

# Check if the bot is already running
if pgrep -f "python run.py" > /dev/null; then
    echo "Bot is already running. Stopping it first..."
    pkill -f "python run.py"
    sleep 2
fi

# Run the application
echo "Starting the Deriv Trading Bot with Gunicorn..."
python run.py &

echo "===== Setup Complete ====="
echo "The bot is now running in the background."
echo "To check logs, use: tail -f gunicorn-access.log gunicorn-error.log"
echo "To stop the bot, use: pkill -f 'python run.py'"
"""