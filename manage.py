#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from decouple import config

def load_env():
    """Load environment variables from .env"""
    try:
        from pathlib import Path
        env_path = Path('.') / '.env'
        env_path.resolve(strict=True)
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
        os.environ['EMAIL_HOST_USER'] = config('EMAIL_HOST_USER')
        os.environ['EMAIL_HOST_PASSWORD'] = config('EMAIL_HOST_PASSWORD')
    except FileNotFoundError:
        print(".env file not found. Make sure to create it.")

def main():
    """Run administrative tasks."""
    load_env()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
