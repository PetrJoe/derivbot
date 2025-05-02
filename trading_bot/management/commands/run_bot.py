from django.core.management.base import BaseCommand
from trading_bot.bot import run_telegram_bot
import logging

logger = logging.getLogger('trading_bot')

class Command(BaseCommand):
    help = 'Run the Deriv Trading Signal Bot'

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS('Starting Deriv Trading Signal Bot...'))
            logger.info("Starting Deriv Trading Signal Bot...")
            run_telegram_bot()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Fatal error: {str(e)}'))
            logger.error(f"Fatal error: {str(e)}")
