#!/usr/bin/env python
from fabric.api import local
import os

HOME_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
MANAGE_SCRIPT = HOME_DIR + "/manage.py"


if __name__ == "__main__":
    local(MANAGE_SCRIPT + " syncdb")
    local(MANAGE_SCRIPT + " migrate")