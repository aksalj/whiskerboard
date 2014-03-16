#!/usr/bin/env python
try:
    import sys
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.contrib.auth.models import User
    from django.core.management import setup_environ
    from django.conf import settings

    u = User.objects.get(username__exact=sys.argv[1])
    u.set_password(sys.argv[2])
    u.save()
except:
    raise

