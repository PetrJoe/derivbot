from django.http import JsonResponse
from django.views.decorators.http import require_GET
import os
import json
from datetime import datetime

@require_GET
def bot_status(request):
    """Return the status of the trading bot"""
    try:
        # Check if the bot is running
        # This is a simple implementation - you might want to use a more robust method
        bot_running = os.path.exists('bot_heartbeat.txt')
        
        # Get the last analysis time if available
        last_analysis_time = None
        if os.path.exists('last_analysis.json'):
            with open('last_analysis.json', 'r') as f:
                data = json.load(f)
                last_analysis_time = data.get('timestamp')
                last_analysis_time = data.get('timestamp')
        
        return JsonResponse({
            'status': 'running' if bot_running else 'stopped',
            'last_analysis': last_analysis_time,
            'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'version': '1.0.0'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'error': str(e)
        }, status=500)
