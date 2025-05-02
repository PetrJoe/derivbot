import os
import sys
import subprocess
import threading
import time
import signal

def run_django():
    print("Starting Django with Gunicorn...")
    subprocess.run(["gunicorn", "--config", "gunicorn_config.py", "deriv.wsgi:application"])

def run_bot():
    print("Starting Trading Bot...")
    subprocess.run([sys.executable, "manage.py", "run_bot"])

def main():
    # Start Django in a separate thread
    django_thread = threading.Thread(target=run_django)
    django_thread.daemon = True
    django_thread.start()
    
    # Give Django some time to start
    time.sleep(5)
    
    # Start the bot in the main thread
    try:
        run_bot()
    except KeyboardInterrupt:
        print("Shutting down...")
    
    # Wait for Django thread to finish
    django_thread.join(timeout=5)

if __name__ == "__main__":
    main()
