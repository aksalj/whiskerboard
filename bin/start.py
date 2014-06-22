#!/usr/bin/env python
from fabric.api import local, env
import os
import sys
import random

"""
Start Whiskerboard
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

    # TODO: Check if running local or live to set DB and IP/PORT
    os.environ['WB_DB_NAME'] = HOME_DIR + "/data/whiskerboard.db"
    os.environ['WB_DB_USER'] = "whiskerboard"
    os.environ['WB_DB_PASSWORD'] = "whiskerboard"
    os.environ['WB_DB_HOST'] = ""
    os.environ['WB_DB_PORT'] = ""


def run():
    setup()
    local(MANAGE_SCRIPT + " collectstatic --noinput")
    local(MANAGE_SCRIPT + " syncdb")
    local(MANAGE_SCRIPT + " migrate")



    runServer = MANAGE_SCRIPT + " runserver"
    for num in range(1, len(sys.argv)): runServer += " " + sys.argv[num]
    local(runServer)


if __name__ == "__main__":
    run()