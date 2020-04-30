from django.db import models
import uuid
from cities.models import City
from django.conf import settings
from django.contrib.postgres.indexes import BrinIndex
from pilkit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from ad_posts.helpers import upload_to_user_directory
from django.contrib.postgres.indexes import BrinIndex


class Course(models.Model):
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
    level = models.CharField(max_length=50, choices = LEVEL, verbose_name="Уровень мастерства")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Город")
    category = models.ForeignKey('skill_categories.SkillSubCategory', on_delete=models.CASCADE, verbose_name="Категория")
    image = ProcessedImageField(format='JPEG', options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])
    video = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ссылка на вводный видео-ролик")
    is_active = models.BooleanField(default=False, verbose_name='Курс активен')
    is_deleted = models.BooleanField(default=False, verbose_name='Курс удален')
    is_private = models.BooleanField(default=False, verbose_name='Курс приватный')
    is_free = models.BooleanField(default=False, verbose_name='Курс бесплатный')
    is_one = models.BooleanField(default=False, verbose_name='Индивидуальный курс')

    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Время публикации")
    data_start = models.DateTimeField(null=True, blank=True, verbose_name="Время начала")
    data_end = models.DateTimeField(null=True, blank=True, verbose_name="Время конца")

    is_reklama = models.BooleanField(default=False, verbose_name='Это реклама')
    votes_off = models.BooleanField(default=False, verbose_name='Лайки-дизлайки отключены')

    def __str__(self):
        return self.title

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering=["-created"]

    def all_visits_count(self):
        from stst.models import CourseNumbers

        return CourseNumbers.objects.filter(course=self.pk).values('pk').count()

    def likes(self):
        from common.model.votes import CourseVotes
        likes = CourseVotes.objects.filter(parent=self, vote__gt=0)
        return likes

    def dislikes(self):
        from common.model.votes import CourseVotes
        dislikes = CourseVotes.objects.filter(parent=self, vote__lt=0)
        return dislikes


class CourseFavourites(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='course_favorites', on_delete=models.CASCADE, verbose_name="Пользователь")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Дата добавления")

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Избранная анкета"
        verbose_name_plural = "Избранные анкеты"
        unique_together = ('course', 'user',)
        indexes = (BrinIndex(fields=['created']),)
