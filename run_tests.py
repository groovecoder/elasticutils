#!/usr/bin/env python

import os
import sys

import nose


# Set up the environment for our test project.
ROOT = os.path.abspath(os.path.dirname(__file__))

try:
    # import to check for the existence of Django
    import django
    os.environ.update({'DJANGO_SETTINGS_MODULE': 'test_settings'})
    sys.path.insert(0, ROOT)

    # This can't be imported until after we've fiddled with the
    # environment.
    from django.test.utils import setup_test_environment
    setup_test_environment()
except ImportError:
    # If django is not found, the Django tests will be skipped, so this is ok.
    pass

# Run nose.
#
# nose.run() returns True if tests passed and False otherwise which is
# the inverse of what we want the process to return, so we invert it.
sys.exit(not nose.run())
