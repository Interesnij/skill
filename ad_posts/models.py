from django.db import models
import uuid
from ad_category.models import AdSubCategory
from cities.models import City
from django.conf import settings
from django.contrib.postgres.indexes import BrinIndex
from pilkit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from ad_posts.helpers import upload_to_user_directory
from django.contrib.postgres.indexes import BrinIndex


class Ad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="uuid")
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(max_length=1000, verbose_name="Описание товара")
    price = models.PositiveIntegerField(default=0, verbose_name="Цена товара")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город")
    category = models.ForeignKey(AdSubCategory, on_delete=models.CASCADE, verbose_name="Ккатегория")
    image = ProcessedImageField(format='JPEG', options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])
    is_active=models.BooleanField(default=False, verbose_name='Объявление опубликовано')
    is_deleted=models.BooleanField(default=False, verbose_name='Объявление удалено')
    is_sold=models.BooleanField(default=False, verbose_name='Объявление не актуально')
    posted=models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Время публикации")
    is_reklama=models.BooleanField(default=False, verbose_name='Это реклама')

    def __str__(self):
        return self.title

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление")
    image = ProcessedImageField(format='JPEG', options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])


class AdDesign(models.Model):
    ad = models.OneToOneField(Ad, db_index=False, on_delete=models.CASCADE, verbose_name="Объявление")
    color = models.CharField(max_length=10, verbose_name="Цвет текста")
    background = models.CharField(max_length=10, verbose_name="Цвет фона")
