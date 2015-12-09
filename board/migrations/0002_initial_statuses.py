# encoding: utf-8
from django.db import migrations, models


def forwards(apps, schema_editor):
    if not schema_editor.connection.alias == 'default':
        return
    # Your migration code goes here

    model = apps.get_model('board', 'Status')

    model.objects.create(
        name="Down",
        slug="down",
        image="cross-circle",
        severity=40,
        description="The service is currently down"
    )
    model.objects.create(
        name="Up",
        slug="up",
        image="tick-circle",
        severity=10,
        description="The service is up"
    )
    model.objects.create(
        name="Warning",
        slug="warning",
        image="exclamation",
        severity=30,
        description="The service is experiencing intermittent problems"
    )


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial')
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
