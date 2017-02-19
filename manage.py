#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "AzureFresh.settings"
    )

    from django.core.management import execute_from_command_line
    #sys.argv = ['C:\\Users\\Owner\\S...manage.py', 'runserver', '--noreload', '--settings', 'PyCon2015AzureTutor....settings', '61928']
    execute_from_command_line(sys.argv)
