# encoding: utf-8
import os
from django.db import migrations
from django.contrib.auth.models import User


def forwards(apps, schema_editor):
    if not schema_editor.connection.alias == 'default':
        return

    # Create initial admin
    username = os.getenv('ADMIN_USER', 'admin')
    email = os.getenv('ADMIN_EMAIL', 'admin@localhost')
    pwd = os.getenv('ADMIN_PASSWORD', 'admin')
    User.objects.create_superuser(username, email, pwd)


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial')
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
