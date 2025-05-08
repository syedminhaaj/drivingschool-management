import os
import sys
import webbrowser
from threading import Timer

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8000')

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'driving_school.settings')
    Timer(1, open_browser).start()
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'runserver'])
