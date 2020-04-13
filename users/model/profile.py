from django.utils import timezone
from django.db import models
from django.conf import settings
from pilkit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from ad_posts.helpers import upload_to_user_directory


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True, db_index=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, db_index=False, related_name="profile", verbose_name="Пользователь", on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, blank=True, verbose_name="Биография")
    sity = models.CharField(max_length=100, blank=True, verbose_name="Местоположение")
    status = models.CharField(max_length=100, blank=True, verbose_name="статус-слоган")
    vk_url = models.URLField(blank=True, verbose_name="Ссылка на vk")
    youtube_url = models.URLField(blank=True, verbose_name="Ссылка на youtube")
    facebook_url = models.URLField(blank=True, verbose_name="Ссылка на facebook")
    instagram_url = models.URLField(blank=True, verbose_name="Ссылка на instagram")
    twitter_url = models.URLField(blank=True, verbose_name="Ссылка на twitter")
    avatar = ProcessedImageField(format='JPEG', options={'quality': 80}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=500, upscale=500)]) 


    def __str__(self):
        return self.user

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        index_together = [('id', 'user'),]
