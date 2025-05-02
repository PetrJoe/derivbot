# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run the bot with Gunicorn
python run.py



# # Run Django with Gunicorn
# gunicorn --config gunicorn_config.py deriv.wsgi:application

# # Run the bot in a separate terminal
# python manage.py run_bot



# # Copy the service file to systemd directory
# sudo cp deriv-trading-bot.service /etc/systemd/system/

# # Enable and start the service
# sudo systemctl enable deriv-trading-bot
# sudo systemctl start deriv-trading-bot

# # Check status
# sudo systemctl status deriv-trading-bot



