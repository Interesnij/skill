from django.db import models
from django.contrib.postgres.indexes import BrinIndex
from django.conf import settings


class AdManageLog(models.Model):
    ACTION_TYPES = (
        ('A', 'Активировано'),
        ('UA', 'Деактивировано'),
        ('D', 'Удалено'),
        ('UD', 'Восстановлено'),
        ('DC', 'Удалён комментарий'),
        ('COFF', 'Отключены комментарии'),
        ('CON', 'Включены комментарии'),
        ('VOFF', 'Отключены реакции'),
        ('VON', 'Включены реакции'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Модератор")
    ad = models.ForeignKey("ad_posts.Ad", on_delete=models.CASCADE, verbose_name="Объявление")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=5)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог объявлений"
        verbose_name_plural = "Логи объявлений"
        ordering=["-created"]
