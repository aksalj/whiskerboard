#!/usr/bin/env python
from fabric.api import local, env
import os
import random

"""
Setup Whiskerboard
"""

HOME_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
SETTINGS_DIR = HOME_DIR + "/settings/"
MANAGE_SCRIPT = HOME_DIR + "/manage.py"


def app(app):
    env['app'] = app


def setup():
    if not os.path.exists(SETTINGS_DIR + 'local.py'):
        with open(SETTINGS_DIR + 'local.py', 'w') as fp:
            secret_key = ''.join([
                random.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
                for i in range(50)
            ])
            fp.write('SECRET_KEY = "%s"\n' % secret_key)

if __name__ == "__main__":
    setup()
    local(MANAGE_SCRIPT + " collectstatic --noinput")
    local(MANAGE_SCRIPT + " syncdb")
    local(MANAGE_SCRIPT + " migrate")