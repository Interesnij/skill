# Generated by Django 2.2.12 on 2020-04-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
