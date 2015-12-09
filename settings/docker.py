from base import *
import imp
#
# Sample docker settings
#
'''
# TODO: Turn off debug
DEBUG = True

if not DEBUG:
    ALLOWED_HOSTS = [
        # IMPORTANT: See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
        'status.example.com'
    ]

# Override SECRET_KEY
SECRET_KEY = os.environ['SECRET_KEY']

# Override DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['MYSQL_DATABASE'],
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'HOST': 'db',  # host name from /etc/hosts
        'PORT': 3306,
    }
}
'''