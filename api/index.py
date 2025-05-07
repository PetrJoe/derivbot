import os
import sys

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the WSGI application
from deriv.wsgi import application

# Export the WSGI application as app
app = application
