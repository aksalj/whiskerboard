# encoding: utf-8
from django.db import migrations, models


def forwards(apps, schema_editor):
    if not schema_editor.connection.alias == 'default':
        return
    # TODO: Create initial users


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial')
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
