from django.db import models
import uuid
from cities.models import City
from django.conf import settings
from django.contrib.postgres.indexes import BrinIndex
from pilkit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from ad_posts.helpers import upload_to_user_directory
from django.contrib.postgres.indexes import BrinIndex


class Cource(models.Model):
    LEVEL=(
        ('Начальный уровень','Начальный уровень'),
        ('Средний уровень','Средний уровень'),
        ('Профессиональный уровень','Профессиональный уровень'),
        ('Все уровни','Все уровни'),
    )

    id = models.BigIntegerField(unique=True, primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="uuid")
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(max_length=1000, verbose_name="Описание курса")
    price = models.PositiveIntegerField(default=0, verbose_name="Цена курса")
    price_acc = models.PositiveIntegerField(default=0, verbose_name="Цена курса со скидкой")
    level = models.CharField(max_length=50, choices = LEVEL, verbose_name="Цена курса со скидкой")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Город")
    category = models.ForeignKey('skill_categories.SkillSubCategory', on_delete=models.CASCADE, verbose_name="Категория")
    image = ProcessedImageField(format='JPEG', options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])
    is_active = models.BooleanField(default=False, verbose_name='Курс активен')
    is_deleted = models.BooleanField(default=False, verbose_name='Курс удален')
    is_private = models.BooleanField(default=False, verbose_name='Курс приватный')
    is_free = models.BooleanField(default=False, verbose_name='Курс бесплатный')
    is_one = models.BooleanField(default=False, verbose_name='Индивидуальный курс')

    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Время публикации")
    data_start = models.DateTimeField(null=True, blank=True, verbose_name="Время начала")
    data_end = models.DateTimeField(null=True, blank=True, verbose_name="Время конца")

    is_reklama = models.BooleanField(default=False, verbose_name='Это реклама')

    def __str__(self):
        return self.title

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering=["-created"]
