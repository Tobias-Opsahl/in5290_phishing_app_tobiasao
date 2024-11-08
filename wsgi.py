import sys
import os
from pathlib import Path

# Add your project directory to the Python path
project_home = str(Path(__file__).resolve().parent)
if project_home not in sys.path:
    sys.path.append(project_home)

# Activate the virtual environment
activate_this = os.path.join(project_home, "myvenv/bin/activate_this.py")
exec(open(activate_this).read(), {'__file__': activate_this})

# Import your Flask app
from app import app as application
