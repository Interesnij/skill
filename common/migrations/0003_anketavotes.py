# Generated by Django 2.2.12 on 2020-04-30 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('love_posts', '0002_auto_20200430_1729'),
        ('common', '0002_coursevotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnketaVotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(choices=[(-1, 'Не нравится'), (1, 'Нравится')], default=0, verbose_name='Голос')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='love_posts.Anketa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
