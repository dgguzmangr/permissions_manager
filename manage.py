#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Check if the 'runserver' command is being executed
    if 'runserver' in sys.argv:
        # Find the index of 'runserver'
        try:
            runserver_index = sys.argv.index('runserver')
        except ValueError:
            runserver_index = None
        
        # If 'runserver' is found, replace the next argument with the default port 8000
        if runserver_index is not None and runserver_index + 1 < len(sys.argv):
            sys.argv[runserver_index + 1] = '8000'
        else:
            # If 'runserver' is not found or there is no next argument, append the default port 8000
            sys.argv.append('8000')
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
