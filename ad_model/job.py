from django.db import models
from ad_posts.models import Ad


class Job(Ad):
    REC_EXP =(
        ('Без опыта работы','Без опыта работы'),
        ('Меньше года','Меньше года'),
        ('От 1 до 3 лет','От 1 до 3 лет'),
        ('От 3 до 5 лет','От 3 до 5 лет'),
        ('Больше 5 лет','Больше 5 лет'),
    )
    WORKS_SHEDULE =(
        ('Полный день','Полный день'),
        ('Сменный график','Сменный график'),
        ('Гибкий график','Гибкий график'),
        ('Удаленная работа','Удаленная работа'),
        ('Вахтовый метод','Вахтовый метод'),
        ('Не полный день','Не полный день'),
    )
    TYPE_EMPLOYMENT =(
        ('Полная занятость','Полная занятость'),
        ('Частичная занятость','Частичная занятость'),
        ('Проектная/временная работа','Проектная/временная работа'),
        ('Волонтерство','Волонтерство'),
        ('Стажировка','Стажировка'),
        ('Временная работа','Временная работа'),
    )
    NATURE_WORK =(
        ('На точке','На точке'),
        ('Офисная','Офисная'),
        ('Разездная','Разездная'),
        ('На дому','На дому'),
    )
    MONEY =(
        ('Почасовая','Почасовая'),
        ('Ежедневная','Ежедневная'),
        ('Ежемесячная','Ежемесячная'),
    )
    OTHER =(
        ('Срочно требуется','Срочно требуется'),
        ('Можно до 18 лет','Можно до 18 лет'),
        ('Необходима мед. книжка','Необходима мед. книжка'),
    )

    required_experience = models.CharField(max_length=50, blank=True, choices = REC_EXP, verbose_name="Требуемый опыт")
    work_schedule = models.CharField(max_length=50, blank=True, choices = WORKS_SHEDULE, verbose_name="График работы")
    type_of_employment = models.CharField(max_length=50, blank=True, choices = TYPE_EMPLOYMENT, verbose_name="Тип занятости")
    nature_work = models.CharField(max_length=50, blank=True, choices = NATURE_WORK, verbose_name="Характер работы")
    money = models.CharField(max_length=50, blank=True, choices = MONEY, verbose_name="Заработная плата")
    other = models.CharField(max_length=50, blank=True, choices = OTHER, verbose_name="Другие условия")
    company = models.CharField(max_length=100, blank=True, verbose_name="Компания")
    pay = models.CharField(max_length=100, blank=True, verbose_name="Зарплата")

    class Meta:
        verbose_name = "Вакансии"
        verbose_name_plural = "Вакансии"
