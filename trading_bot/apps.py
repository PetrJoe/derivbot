from django.apps import AppConfig
import os

class TradingBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trading_bot'
    
    def ready(self):
        # Create a heartbeat file to indicate the app is running
        with open('bot_heartbeat.txt', 'w') as f:
            f.write('running')
        
        # Create static directory if it doesn't exist
        os.makedirs('static', exist_ok=True)
