from django.db import models
import uuid
from cities.models import City
from django.conf import settings
from django.contrib.postgres.indexes import BrinIndex
from pilkit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from ad_posts.helpers import upload_to_user_directory


class Ad(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="uuid")
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(max_length=1000, verbose_name="Описание товара")
    price = models.PositiveIntegerField(default=0, verbose_name="Цена товара")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город")
    category = models.ForeignKey('ad_categories.AdSubCategory', on_delete=models.CASCADE, verbose_name="Ккатегория")
    is_active = models.BooleanField(default=False, verbose_name='Объявление опубликовано')
    is_deleted = models.BooleanField(default=False, verbose_name='Объявление удалено')
    is_sold = models.BooleanField(default=False, verbose_name='Объявление не актуально')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Время публикации")
    is_reklama = models.BooleanField(default=False, verbose_name='Это реклама')
    votes_off = models.BooleanField(default=False, verbose_name='отключить лайки/дизлайки')

    image = ProcessedImageField(format='JPEG', blank=True, options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])
    img1 = ProcessedImageField(format='JPEG', blank=True, options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])
    img2 = ProcessedImageField(format='JPEG', blank=True, options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])
    img3 = ProcessedImageField(format='JPEG', blank=True, options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])
    img4 = ProcessedImageField(format='JPEG', blank=True, options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])
    img5 = ProcessedImageField(format='JPEG', blank=True, options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])
    img6 = ProcessedImageField(format='JPEG', blank=True, options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])
    img7 = ProcessedImageField(format='JPEG', blank=True, options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])

    def __str__(self):
        return self.title

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering=["-created"]

    def all_visits_count(self):
        from stst.models import AdNumbers

        return AdNumbers.objects.filter(ad=self.pk).values('pk').count()

    def likes(self):
        from common.model.votes import AdVotes
        likes = AdVotes.objects.filter(parent=self, vote__gt=0)
        return likes

    def likes_count(self):
        from common.model.votes import AdVotes
        likes = AdVotes.objects.filter(parent=self, vote__gt=0).values("pk")
        return likes.count()

    def dislikes(self):
        from common.model.votes import AdVotes
        dislikes = AdVotes.objects.filter(parent=self, vote__lt=0)
        return dislikes

    def dislikes_count(self):
        from common.model.votes import AdVotes
        dislikes = AdVotes.objects.filter(parent=self, vote__lt=0).values("pk")
        return dislikes.count()


class AdDesign(models.Model):
    ad = models.OneToOneField(Ad, db_index=False, on_delete=models.CASCADE, verbose_name="Объявление")
    color = models.CharField(max_length=10, verbose_name="Цвет текста")
    background = models.CharField(max_length=10, verbose_name="Цвет фона")


class AdFavourites(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ad_favorites', on_delete=models.CASCADE, verbose_name="Пользователь")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Дата добавления")

    def __str__(self):
        return self.ad.title

    class Meta:
        verbose_name = "Избранное объявление"
        verbose_name_plural = "Избранные объявления"
        unique_together = ('ad', 'user',)
        indexes = (BrinIndex(fields=['created']),)
