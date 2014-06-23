from base import *
import imp
#
# Sample cloud settings (for OpenShift)
# See https://github.com/openshift/django-example
#

'''

# Turn off debug
DEBUG = False

if not DEBUG:
    ALLOWED_HOSTS = [
        # IMPORTANT: See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
        'status.aksalj.me'
    ]


# Load the OpenShift helper library
lib_path = os.environ['OPENSHIFT_REPO_DIR'] + 'libs/'
modinfo = imp.find_module('openshiftlibs', [lib_path])
openshiftlibs = imp.load_module('openshiftlibs', modinfo[0], modinfo[1], modinfo[2])

# Override SECRET_KEY
# Make a dictionary of default keys
default_keys = {'SECRET_KEY': SECRET_KEY}
# Replace default keys with dynamic values
use_keys = openshiftlibs.openshift_secure(default_keys)
# Make this unique, and don't share it with anybody.
SECRET_KEY = use_keys['SECRET_KEY']


# Override DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'sqlite3.db'),
        'USER': 'whiskerboard',
        'PASSWORD': '6Z75kPBNmrIswBDdrsIT',
        'HOST': '',
        'PORT': '',
    }
}

# Override STATIC_ROOT
STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static')

'''