#!/usr/bin/env python
from fabric.api import local
import os
import sys

"""
Start Whiskerboard
"""

HOME_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
MANAGE_SCRIPT = HOME_DIR + "/manage.py"


if __name__ == "__main__":
    runServer = MANAGE_SCRIPT + " runserver"
    for num in range(1, len(sys.argv)): runServer += " " + sys.argv[num]
    local(runServer)