# Generated by Django 2.2.12 on 2020-04-26 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stst', '0002_auto_20200426_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursenumbers',
            old_name='skill',
            new_name='course',
        ),
    ]
