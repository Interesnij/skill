# Generated by Django 2.2.12 on 2020-04-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_posts', '0003_auto_20200417_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='votes_off',
            field=models.BooleanField(default=False, verbose_name='Лайки-дизлайки отключены'),
        ),
    ]