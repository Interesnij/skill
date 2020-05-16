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
        verbose_name = "Лог пользоватетей"
        verbose_name_plural = "Логи пользоватетей"
        ordering=["-created"]


class AdWorkerLog(models.Model):
    ACTION_TYPES = (
        ('Добавлен админ объявлений', 'Добавлен админ объявлений'),
        ('Удален админ объявлений', 'Удален админ объявлений'),
        ('Добавлен модератор объявлений', 'Добавлен модератор объявлений'),
        ('Удален модератор объявлений', 'Удален модератор объявлений'),
        ('Добавлен редактор объявлений', 'Добавлен редактор объявлений'),
        ('Удален редактор объявлений', 'Удален редактор объявлений'),
        ('Добавлен рекламодатель объявлений', 'Добавлен рекламодатель объявлений'),
        ('Удален рекламодател объявлений', 'Удален рекламодатель объявлений'),
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
        ('Добавлен админ академии', 'Добавлен админ академии'),
        ('Удален админ академии', 'Удален админ академии'),
        ('Добавлен модератор академии', 'Добавлен модератор академии'),
        ('Удален модератор академии', 'Удален модератор академии'),
        ('Добавлен редактор академии', 'Добавлен редактор академии'),
        ('Удален редактор академии', 'Удален редактор академии'),
        ('Добавлен рекламодатель академии', 'Добавлен рекламодатель академии'),
        ('Удален рекламодател академии', 'Удален рекламодатель академии'),
        ('Добавлен учитель академии', 'Добавлен учитель академии'),
        ('Удален учитель академии', 'Удален учитель академии'),
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
        ('Добавлен админ знакомств', 'Добавлен админ знакомств'),
        ('Удален админ знакомств', 'Удален админ знакомств'),
        ('Добавлен модератор знакомств', 'Добавлен модератор знакомств'),
        ('Удален модератор знакомств', 'Удален модератор знакомств'),
        ('Добавлен редактор знакомств', 'Добавлен редактор знакомств'),
        ('Удален редактор знакомств', 'Удален редактор знакомств'),
        ('Добавлен рекламодатель знакомств', 'Добавлен рекламодатель знакомств'),
        ('Удален рекламодатель знакомств', 'Удален рекламодатель знакомств'),
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
        ('Добавлен админ пользователей', 'Добавлен админ пользователей'),
        ('Удален админ пользователей', 'Удален админ пользователей'),
        ('Добавлен модератор пользователей', 'Добавлен модератор пользователей'),
        ('Удален модератор пользователей', 'Удален модератор пользователей'),
        ('Добавлен редактор пользователей', 'Добавлен редактор пользователей'),
        ('Удален редактор пользователей', 'Удален редактор пользователей'),
        ('Добавлен рекламодатель пользователей', 'Добавлен рекламодатель пользователей'),
        ('Удален рекламодатель пользователей', 'Удален рекламодатель пользователей'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_manag", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог менеджера пользователей"
        verbose_name_plural = "Логи менеджеров пользователей"
        ordering=["-created"]


class AdManageCreatorLog(models.Model):
    ACTION_TYPES = (
        ('Добавлен создатель админов объявлений', 'Добавлен создатель админов объявлений'),
        ('Удален создатель админов объявлений', 'Удален создатель админов объявлений'),
        ('Добавлен создатель редакторов объявлений', 'Добавлен создатель редакторов объявлений'),
        ('Удален создатель редакторов объявлений', 'Удален создатель редакторов объявлений'),
        ('Добавлен создатель модераторов объявлений', 'Добавлен создатель модераторов объявлений'),
        ('Удален создатель модераторов объявлений', 'Удален создатель модераторов объявлений'),
        ('Добавлен создатель рекламодателей объявлений', 'Добавлен создатель рекламодателей объявлений'),
        ('Удален создатель рекламодателей объявлений', 'Удален создатель рекламодателей объявлений'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_ad_creator_manage", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог созлателя персонала объявлений"
        verbose_name_plural = "Логи созлателей персонала объявлений"
        ordering=["-created"]


class SkillManageCreatorLog(models.Model):
    ACTION_TYPES = (
        ('Добавлен создатель админов академии', 'Добавлен создатель админов академии'),
        ('Удален создатель админов академии', 'Удален создатель админов академии'),
        ('Добавлен создатель редакторов академии', 'Добавлен создатель редакторов академии'),
        ('Удален создатель редакторов академии', 'Удален создатель редакторов академии'),
        ('Добавлен создатель модераторов академии', 'Добавлен создатель модераторов академии'),
        ('Удален создатель модераторов академии', 'Удален создатель модераторов академии'),
        ('Добавлен создатель рекламодателей академии', 'Добавлен создатель рекламодателей академии'),
        ('Удален создатель рекламодателей академии', 'Удален создатель рекламодателей академии'),
        ('Добавлен создатель учителей академии', 'Добавлен создатель учителей академии'),
        ('Удален создатель учителей академии', 'Удален создатель учителей академии'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_skill_creator_manage", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог созлателя персонала академии"
        verbose_name_plural = "Логи созлателей персонала академии"
        ordering=["-created"]


class AnketaManageCreatorLog(models.Model):
    ACTION_TYPES = (
        ('Добавлен создатель админов знакомств', 'Добавлен создатель админов знакомств'),
        ('Удален создатель админов знакомств', 'Удален создатель админов знакомств'),
        ('Добавлен создатель редакторов знакомств', 'Добавлен создатель редакторов знакомств'),
        ('Удален создатель редакторов знакомств', 'Удален создатель редакторов знакомств'),
        ('Добавлен создатель модераторов знакомств', 'Добавлен создатель модераторов знакомств'),
        ('Удален создатель модераторов знакомств', 'Удален создатель модераторов знакомств'),
        ('Добавлен создатель рекламодателей знакомств', 'Добавлен создатель рекламодателей знакомств'),
        ('Удален создатель рекламодателей знакомств', 'Удален создатель рекламодателей знакомств'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_anketa_creator_manage", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог созлателя персонала знакомств"
        verbose_name_plural = "Логи созлателей персонала знакомств"
        ordering=["-created"]


class UserManageCreatorLog(models.Model):
    ACTION_TYPES = (
        ('Добавлен создатель админов пользователей', 'Добавлен создатель админов пользователей'),
        ('Удален создатель админов пользователей', 'Удален создатель админов пользователей'),
        ('Добавлен создатель редакторов пользователей', 'Добавлен создатель редакторов пользователей'),
        ('Удален создатель редакторов пользователей', 'Удален создатель редакторов пользователей'),
        ('Добавлен создатель модераторов пользователей', 'Добавлен создатель модераторов пользователей'),
        ('Удален создатель модераторов пользователей', 'Удален создатель модераторов пользователей'),
        ('Добавлен создатель рекламодателей пользователей', 'Добавлен создатель рекламодателей пользователей'),
        ('Удален создатель рекламодателей пользователей', 'Удален создатель рекламодателей пользователей'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_creator_manage", on_delete=models.CASCADE, verbose_name="Менеджер")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    action_type = models.CharField(editable=False, blank=False, null=False, choices=ACTION_TYPES, max_length=50)

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Лог созлателя персонала пользователей"
        verbose_name_plural = "Логи созлателей персонала пользователей"
        ordering=["-created"]
