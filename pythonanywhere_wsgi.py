"""
Copy this file's contents into your PythonAnywhere Web → WSGI configuration file.
Username: cloudcity
Free URL: https://cloudcity.pythonanywhere.com
"""
import sys

# Folder that contains app.py (adjust only if you uploaded elsewhere)
project_home = "/home/cloudcity/cloudcity"

if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Optional: set once in a Bash console with:
#   export CLOUFCITY_SECRET='some-long-random-string'
# Or leave default for free testing.
from app import app as application
