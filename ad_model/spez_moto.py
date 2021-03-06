from django.db import models
from ad_posts.models import Ad


class SpecMoto(Ad):
    BUSES_TRUCKS=(
        ('Автобусы','Автобусы'),
        ('Микроавтобусы','Микроавтобусы'),
        ('Автодома','Автодома'),
        ('Авторефрижераторы','Авторефрижераторы'),
        ('Грузовики, шасси','Грузовики, шасси'),
        ('Грузовые прицепы','Грузовые прицепы'),
        ('Седельные тягачи','Седельные тягачи'),
    )
    WOTER_TRANSPORT=(
        ('Гидроциклы','Гидроциклы'),
        ('Гребные лодки','Гребные лодки'),
        ('Катера, яхты','Катера, яхты'),
        ('Моторные лодки','Моторные лодки'),
        ('Надувные лодки','Надувные лодки'),
        ('Лодочные моторы, запчасти','Лодочные моторы, запчасти'),
    )
    MOTORTECHNIQUE=(
        ('Дорожные мотоциклы','Дорожные мотоциклы'),
        ('Спортивные мотоциклы','Спортивные мотоциклы'),
        ('Кросс, эндуро','Кросс, эндуро'),
        ('Круизеры, чопперы','Круизеры, чопперы'),
        ('Кастом-байки','Кастом-байки'),
        ('Мопеды, скутеры','Мопеды, скутеры'),
        ('Квадроциклы','Квадроциклы'),
        ('Багги','Багги'),
        ('Картинг','Картинг'),
        ('Снегоходы','Снегоходы'),
    )
    SPECIAL_MACHINERY=(
        ('Автовышки','Автовышки'),
        ('Автокраны','Автокраны'),
        ('Бульдозеры','Бульдозеры'),
        ('Вездеходы-амфибии','Вездеходы-амфибии'),
        ('Коммунальная техника','Коммунальная техника'),
        ('Погрузчики','Погрузчики'),
        ('Строительная техника','Строительная техника'),
        ('Техника для лесозаготовки','Техника для лесозаготовки'),
        ('Тракторы, сельхозтехника','Тракторы, сельхозтехника'),
        ('Экскаваторы','Экскаваторы'),
    )

    buses_trucks = models.CharField(max_length=50, blank=True, choices = BUSES_TRUCKS, verbose_name="Автобусы и грузовики")
    motortechnique = models.CharField(max_length=50, blank=True, choices = WOTER_TRANSPORT, verbose_name="Водный транспорт")
    motor = models.CharField(max_length=50, blank=True, choices = MOTORTECHNIQUE, verbose_name="Мототехника")
    special_machinery = models.CharField(max_length=50, blank=True, choices = SPECIAL_MACHINERY, verbose_name="Спецтехника")

    class Meta:
        verbose_name = "Спецтехника и мотоциклы"
        verbose_name_plural = "Спецтехника и мотоциклы"
