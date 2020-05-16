from django.db import models
from django.contrib.postgres.indexes import BrinIndex
from django.conf import settings


class AdManageLog(models.Model):
    ACTION_TYPES = (
        ('Активировано', 'Активировано'),
        ('Деактивировано', 'Деактивировано'),
        ('Удалено', 'Удалено'),
        ('Восстановлено', 'Восстановлено'),
        ('Удалён комментарий', 'Удалён комментарий'),
        ('Отключены комментарии', 'Отключены комментарии'),
        ('Включены комментарии', 'Включены комментарии'),
        ('Отключены реакции', 'Отключены реакции'),
        ('Включены реакции', 'Включены реакции'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Модератор")
    ad = models.ForeignKey("ad_posts.Ad", on_delete=models.CASCADE, verbose_name="Объявление")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог объявлений"
        verbose_name_plural = "Логи объявлений"
        ordering=["-created"]


class SkillManageLog(models.Model):
    ACTION_TYPES = (
        ('Активирован', 'Активирован'),
        ('Деактивирован', 'Деактивирован'),
        ('Удален', 'Удален'),
        ('Восстановлен', 'Восстановлен'),
        ('Удалён комментарий', 'Удалён комментарий'),
        ('Отключены комментарии', 'Отключены комментарии'),
        ('Включены комментарии', 'Включены комментарии'),
        ('Отключены реакции', 'Отключены реакции'),
        ('Включены реакции', 'Включены реакции'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Модератор")
    course = models.ForeignKey("skill_posts.Course", on_delete=models.CASCADE, verbose_name="Курс")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог курсов"
        verbose_name_plural = "Логи курсов"
        ordering=["-created"]


class AnketaManageLog(models.Model):
    ACTION_TYPES = (
        ('Активирован', 'Активирован'),
        ('Деактивирован', 'Деактивирован'),
        ('Удален', 'Удален'),
        ('Восстановлен', 'Восстановлен'),
        ('Удалён комментарий', 'Удалён комментарий'),
        ('Отключены комментарии', 'Отключены комментарии'),
        ('Включены комментари', 'Включены комментарии'),
        ('Отключены реакции', 'Отключены реакции'),
        ('Включены реакции', 'Включены реакции'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Модератор")
    anketa = models.ForeignKey("love_posts.Anketa", on_delete=models.CASCADE, verbose_name="Анкета")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог анкеты"
        verbose_name_plural = "Логи анкет"
        ordering=["-created"]


class UserManageLog(models.Model):
    ACTION_TYPES = (
        ('Удален', 'Удален'),
        ('Восстановлен', 'Восстановлен'),
        ('Заблокирован', 'Заблокирован'),
        ('Разблокирован', 'Разблокирован'),
        ('Заморожен', 'Заморожен'),
        ('Разморожен', 'Разморожен'),
        ('Стал техподдержкой', 'Стал техподдержкой'),
        ('Удален из техподдержки', 'Удален из техподдержки'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_manag", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог курсов"
        verbose_name_plural = "Логи курсов"
        ordering=["-created"]


class AdWorkerLog(models.Model):
    ACTION_TYPES = (
        ('Добавлен админ', 'Добавлен админ'),
        ('Удален админ', 'Удален админ'),
        ('Добавлен модератор', 'Добавлен модератор'),
        ('Удален модератор', 'Удален модератор'),
        ('Добавлен редактор', 'Добавлен редактор'),
        ('Удален редактор', 'Удален редактор'),
        ('Добавлен рекламодатель', 'Добавлен рекламодатель'),
        ('Удален рекламодател', 'Удален рекламодатель'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="ad_manager", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог менеджера руководителей объявлений"
        verbose_name_plural = "Лог менеджера руководителей объявлений"
        ordering=["-created"]


class SkillWorkerLog(models.Model):
    ACTION_TYPES = (
        ('Добавлен админ', 'Добавлен админ'),
        ('Удален админ', 'Удален админ'),
        ('Добавлен модератор', 'Добавлен модератор'),
        ('Удален модератор', 'Удален модератор'),
        ('Добавлен редактор', 'Добавлен редактор'),
        ('Удален редактор', 'Удален редактор'),
        ('Добавлен рекламодатель', 'Добавлен рекламодатель'),
        ('Удален рекламодател', 'Удален рекламодатель'),
        ('Добавлен учитель', 'Добавлен учитель'),
        ('Удален учитель', 'Удален учитель'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="skill_manager", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог менеджера руководителей курсов"
        verbose_name_plural = "Логи менеджеров руководителей курсов"
        ordering=["-created"]


class AnketaWorkerLog(models.Model):
    ACTION_TYPES = (
        ('Добавлен админ', 'Добавлен админ'),
        ('Удален админ', 'Удален админ'),
        ('Добавлен модератор', 'Добавлен модератор'),
        ('Удален модератор', 'Удален модератор'),
        ('Добавлен редактор', 'Добавлен редактор'),
        ('Удален редактор', 'Удален редактор'),
        ('Добавлен рекламодатель', 'Добавлен рекламодатель'),
        ('Удален рекламодател', 'Удален рекламодатель'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="anketa_manager", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог менеджера руководителей знакомств"
        verbose_name_plural = "Логи менеджеров руководителей знакомств"
        ordering=["-created"]


class UserWorkerLog(models.Model):
    ACTION_TYPES = (
        ('Добавлен создатель персонала объявлений', 'Добавлен создатель персонала объявлений'),
        ('Удален создатель персонала объявлений', 'Удален создатель персонала объявлений'),
        ('Добавлен создатель персонала курсовCS', 'Добавлен создатель персонала курсов'),
        ('Удален создатель персонала курсов', 'Удален создатель персонала курсов'),
        ('Добавлен создатель персонала знакомств', 'Добавлен создатель персонала знакомств'),
        ('Удален создатель персонала знакомств', 'Удален создатель персонала знакомств'),
        ('Добавлен создатель персонала пользователей', 'Добавлен создатель персонала пользователей'),
        ('Удален создатель персонала пользователей', 'Удален создатель персонала пользователей'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_manager", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог менеджера руководителей"
        verbose_name_plural = "Логи менеджеров руководителей"
        ordering=["-created"]
