# Generated by Django 2.2.12 on 2020-04-23 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100, unique=True, verbose_name='Русское название')),
                ('name_en', models.CharField(max_length=100, unique=True, verbose_name='Английское название')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер')),
                ('image', models.ImageField(blank=True, upload_to='skill_category/cat', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Категория курсов',
                'ordering': ['order'],
                'verbose_name_plural': 'Категории курсов',
            },
        ),
        migrations.CreateModel(
            name='SkillSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Название подкатегории')),
                ('name_en', models.CharField(max_length=100, unique=True, verbose_name='Английское название')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер подкатегории')),
                ('image', models.ImageField(blank=True, upload_to='skill_category/sub', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill_categories.SkillCategory', verbose_name='Категория-родитель')),
            ],
            options={
                'verbose_name': 'суб-категория курсов',
                'verbose_name_plural': 'суб-категории курсов',
            },
        ),
    ]
