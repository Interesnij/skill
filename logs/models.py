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


class SkillManageLog(models.Model):
    ACTION_TYPES = (
        ('A', 'Активирован'),
        ('UA', 'Деактивирован'),
        ('D', 'Удален'),
        ('UD', 'Восстановлен'),
        ('DC', 'Удалён комментарий'),
        ('COFF', 'Отключены комментарии'),
        ('CON', 'Включены комментарии'),
        ('VOFF', 'Отключены реакции'),
        ('VON', 'Включены реакции'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Модератор")
    course = models.ForeignKey("skill_posts.Course", on_delete=models.CASCADE, verbose_name="Курс")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=5)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог курсов"
        verbose_name_plural = "Логи курсов"
        ordering=["-created"]


class AnketaManageLog(models.Model):
    ACTION_TYPES = (
        ('A', 'Активирован'),
        ('UA', 'Деактивирован'),
        ('D', 'Удален'),
        ('UD', 'Восстановлен'),
        ('DC', 'Удалён комментарий'),
        ('COFF', 'Отключены комментарии'),
        ('CON', 'Включены комментарии'),
        ('VOFF', 'Отключены реакции'),
        ('VON', 'Включены реакции'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Модератор")
    anketa = models.ForeignKey("love_posts.Anketa", on_delete=models.CASCADE, verbose_name="Анкета")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=5)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог анкеты"
        verbose_name_plural = "Логи анкет"
        ordering=["-created"]


class AdWorkerLog(models.Model):
    ACTION_TYPES = (
        ('C', 'Повышен'),
        ('UC', 'Разжалован'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="ad_manager", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=5)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог объявлений"
        verbose_name_plural = "Логи объявлений"
        ordering=["-created"]


class SkillWorkerLog(models.Model):
    ACTION_TYPES = (
        ('C', 'Повышен'),
        ('UC', 'Разжалован'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="skill_manager", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=5)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог курсов"
        verbose_name_plural = "Логи курсов"
        ordering=["-created"]


class AnketaWorkerLog(models.Model):
    ACTION_TYPES = (
        ('C', 'Повышен'),
        ('UC', 'Разжалован'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="anketa_manager", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=5)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог курсов"
        verbose_name_plural = "Логи курсов"
        ordering=["-created"]


class UserWorkerLog(models.Model):
    ACTION_TYPES = (
        ('R', 'Удален'),
        ('UR', 'Восстановлен'),
        ('B', 'Заблокирован'),
        ('А', 'Разблокирован'),
        ('F', 'Заморожен'),
        ('UN', 'Разморожен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_manager", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=5)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог курсов"
        verbose_name_plural = "Логи курсов"
        ordering=["-created"]
