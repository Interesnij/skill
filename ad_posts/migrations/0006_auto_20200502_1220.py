# Generated by Django 2.2.12 on 2020-05-02 12:20

import ad_posts.helpers
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ad_posts', '0005_auto_20200430_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='img1',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=ad_posts.helpers.upload_to_user_directory),
        ),
        migrations.AddField(
            model_name='ad',
            name='img2',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=ad_posts.helpers.upload_to_user_directory),
        ),
        migrations.AddField(
            model_name='ad',
            name='img3',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=ad_posts.helpers.upload_to_user_directory),
        ),
        migrations.AddField(
            model_name='ad',
            name='img4',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=ad_posts.helpers.upload_to_user_directory),
        ),
        migrations.AddField(
            model_name='ad',
            name='img5',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=ad_posts.helpers.upload_to_user_directory),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=ad_posts.helpers.upload_to_user_directory),
        ),
        migrations.DeleteModel(
            name='AdImage',
        ),
    ]