from __future__ import absolute_import
import os
from .base import *
from .local import *

# Your live settings go here

"""

DEBUG = False

######################################
# Database - Openshift
######################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ['OPENSHIFT_DATA_DIR'] + 'database.db',
        'USER': "whiskerboard",
        'PASSWORD': "whiskerboard",
        'HOST': "",
        'PORT': "",
    }
}

"""