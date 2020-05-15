# Generated by Django 2.2.12 on 2020-04-14 09:29

import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Кто смотрит')),
                ('ad', models.PositiveIntegerField(default=0, verbose_name='Какое объявления смотрит')),
                ('platform', models.PositiveIntegerField(default=0, verbose_name='0 Комп, 1 Телефон')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name_plural': 'Просмотры объявлений',
                'verbose_name': 'Просмотр объявления',
            },
        ),
        migrations.CreateModel(
            name='SkillNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Кто смотрит')),
                ('skill', models.PositiveIntegerField(default=0, verbose_name='Какой курс смотрит')),
                ('platform', models.PositiveIntegerField(default=0, verbose_name='0 Комп, 1 Телефон')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name_plural': 'Посещения курса',
                'verbose_name': 'Посещение курса',
            },
        ),
        migrations.CreateModel(
            name='UserNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor', models.PositiveIntegerField(default=0, verbose_name='Кто заходит')),
                ('target', models.PositiveIntegerField(default=0, verbose_name='К кому заходит')),
                ('platform', models.PositiveIntegerField(default=0, verbose_name='0 Комп, 1 Телефон')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name_plural': 'Кто к кому заходил',
                'verbose_name': 'Кто к кому заходил',
            },
        ),
        migrations.AddIndex(
            model_name='usernumbers',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='stst_usernu_created_c7bca1_brin'),
        ),
        migrations.AddIndex(
            model_name='skillnumbers',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='stst_skilln_created_006f66_brin'),
        ),
        migrations.AddIndex(
            model_name='adnumbers',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='stst_adnumb_created_6bce11_brin'),
        ),
    ]