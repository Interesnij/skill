from django.db import models
from django.conf import settings
from django.contrib.postgres.indexes import BrinIndex


class UserNumbers(models.Model):
    visitor = models.PositiveIntegerField(default=0, verbose_name="Кто заходит")
    target = models.PositiveIntegerField(default=0, verbose_name="К кому заходит")
    platform = models.PositiveIntegerField(default=0, verbose_name="0 Комп, 1 Телефон")
    created = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Создано")

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name="Кто к кому заходил"
        verbose_name_plural="Кто к кому заходил"


class CourseNumbers(models.Model):
    user = models.PositiveIntegerField(default=0, verbose_name="Кто смотрит")
    course = models.PositiveIntegerField(default=0, verbose_name="Какой курс смотрит")
    platform = models.PositiveIntegerField(default=0, verbose_name="0 Комп, 1 Телефон")
    created = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Создано")

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name="Посещение курса"
        verbose_name_plural="Посещения курса"


class AdNumbers(models.Model):
    user = models.PositiveIntegerField(default=0, verbose_name="Кто смотрит")
    ad = models.PositiveIntegerField(default=0, verbose_name="Какое объявления смотрит")
    platform = models.PositiveIntegerField(default=0, verbose_name="0 Комп, 1 Телефон")
    created = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Создано")

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name="Просмотр объявления"
        verbose_name_plural="Просмотры объявлений"


class AnketaNumbers(models.Model):
    user = models.PositiveIntegerField(default=0, verbose_name="Кто смотрит")
    anketa = models.PositiveIntegerField(default=0, verbose_name="Какое объявления смотрит")
    platform = models.PositiveIntegerField(default=0, verbose_name="0 Комп, 1 Телефон")
    created = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Создано")

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name="Просмотр анкеты"
        verbose_name_plural="Просмотры анкеты"
