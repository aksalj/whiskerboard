from __future__ import absolute_import
from .base import *
from .local import *

#CACHE_BACKEND = 'redis_cache.cache://127.0.0.1:6379/?timeout=15'
DEBUG = False

# Openshift Settings
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': '$OPENSHIFT_DATA/database.db',
    'USER': 'whiskerboard',
    'PASSWORD': 'mHxXFxyTd5N29W9qGYHMbQL6',
    'HOST': '',
    'PORT': '',
}

