# Generated by Django 2.2.12 on 2020-04-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_posts', '0003_auto_20200425_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Начальный уровень', 'Начальный уровень'), ('Средний уровень', 'Средний уровень'), ('Профессиональный уровень', 'Профессиональный уровень'), ('Все уровни', 'Все уровни')], max_length=50, verbose_name='Уровень мастерства'),
        ),
    ]