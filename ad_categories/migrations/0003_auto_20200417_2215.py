# Generated by Django 2.2.12 on 2020-04-17 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad_categories', '0002_auto_20200417_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adcategory',
            options={'ordering': ['order'], 'verbose_name': 'Категория объявлений', 'verbose_name_plural': 'Категории объявлений'},
        ),
    ]