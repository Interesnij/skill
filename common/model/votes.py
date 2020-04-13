from django.db import models
from django.conf import settings


class AdVotes(models.Model):
    LIKE = 1
    DISLIKE = -1
    VOTES = ((DISLIKE, 'Не нравится'),(LIKE, 'Нравится'))

    vote = models.IntegerField(default=0, verbose_name="Голос", choices=VOTES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    parent = models.ForeignKey('ad_posts.Ad', on_delete=models.CASCADE)
