from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.postgres.indexes import BrinIndex
from ad_posts.models import Ad


class Favourites(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Дата добавления")

    def __str__(self):
        return self.ad.title

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"
        unique_together = ('ad', 'user',)
        indexes = (BrinIndex(fields=['created']),)


class ChatAd(models.Model):
    ad = models.ForeignKey(Ad, related_name='chat_ad', on_delete=models.CASCADE, verbose_name="Обсуждаемый товар")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Дата добавления")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Обсуждаемый товар"
        verbose_name_plural = "Обсуждаемый товар"
        indexes = (BrinIndex(fields=['created']),)


class Subscribe(models.Model):
    adding_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="adding_user", on_delete=models.CASCADE, verbose_name="Кто подписался")
    added_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="added_user", on_delete=models.CASCADE, verbose_name="На кого подписался")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Дата добавления")

    def __str__(self):
        return self.adding_user

    class Meta:
        verbose_name = "Подписки"
        verbose_name_plural = "Подписки"
        unique_together = ('adding_user', 'added_user',)
        indexes = (BrinIndex(fields=['created']),)


class Guest(models.Model):
    STAR =(
		('1','Очень плохо'),
		('2','Плохо'),
		('3','Нормально'),
		('4','Хорошо'),
		('5','Отлично'),
	)

    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='guest_sender', verbose_name="Кто написал")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='guest_receiver', verbose_name="Кому написал")
    title = models.CharField(max_length=100, verbose_name="Что понравилось / не понравилось")
    message = models.CharField(max_length=1000, verbose_name="Сообщение")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Дата добавления")
    star = models.CharField(max_length=50, choices=STAR, verbose_name="Рейтинг")

    def __str__(self):
        return self.receiver

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Отзыв на пользователя"
        verbose_name_plural = "Отзывы на пользователя"


class UserBlock(models.Model):
    blocked_user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, on_delete=models.CASCADE, related_name='blocked_by_users', verbose_name="Кого блокирует")
    blocker = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, on_delete=models.CASCADE, related_name='user_blocks', verbose_name="Кто блокирует")

    @classmethod
    def create_user_block(cls, blocker_id, blocked_user_id):
        return cls.objects.create(blocker_id=blocker_id, blocked_user_id=blocked_user_id)

    @classmethod
    def users_are_blocked(cls, user_a_id, user_b_id):
        return cls.objects.filter(Q(blocked_user_id=user_a_id, blocker_id=user_b_id)).exists()

    class Meta:
        unique_together = ('blocked_user', 'blocker',)
        indexes = [models.Index(fields=['blocked_user', 'blocker']),]
