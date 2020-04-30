from django.db import models
import uuid
from cities.models import City
from django.conf import settings
from django.contrib.postgres.indexes import BrinIndex
from pilkit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from ad_posts.helpers import upload_to_user_directory
from django.contrib.postgres.indexes import BrinIndex


class Anketa(models.Model):
    POLITIC=(
        ('Не выбраны','Не выбраны'),
        ('Индиффирентные','Индиффирентные'),
        ('Коммунистические','Коммунистические'),
        ('Социалистические','Социалистические'),
        ('Умеренные','Умеренные'),
        ('Либеральные','Либеральные'),
        ('Консервативные','Консервативные'),
        ('Либералистические','Либералистические'),
        ('Ультраконсервативные','Ультраконсервативные'),
    )
    WORLDVIEW=(
        ('Не выбрано','Не выбрано'),
        ('Иудаизм','Иудаизм'),
        ('Православие','Православие'),
        ('Католицизм','Католицизм'),
        ('Протестантизм','Протестантизм'),
        ('Ислам','Ислам'),
        ('Буддизм','Буддизм'),
        ('Конфуцианство','Конфуцианство'),
        ('Светский гуманизм','Светский гуманизм'),
        ('Пастафарианство','Пастафарианство'),
    )
    MAINTHING_IN_LIFE=(
        ('Не выбрано','Не выбрано'),
        ('Семья и дети','Семья и дети'),
        ('Карьера и деньги','Карьера и деньги'),
        ('Развлечение и отдых','Развлечение и отдых'),
        ('Наука и исследования','Наука и исследования'),
        ('Совершенствование мира','Совершенствование мира'),
        ('Саморазвитие','Саморазвитие'),
        ('Красота и искусство','Красота и искусство'),
        ('Слава и влияние','Слава и влияние'),
    )
    MAINTHING_IN_PEOPLE=(
        ('Не выбрано','Не выбрано'),
        ('Ум и креативность','Ум и креативность'),
        ('Доброта и честность','Доброта и честность'),
        ('Красота и здоровье','Красота и здоровье'),
        ('Власть и богатство','Власть и богатство'),
        ('Смелость и упорство','Смелость и упорство'),
        ('Юмор и жизнелюбие','Юмор и жизнелюбие'),
    )
    ATTITUDE_TO_SMOKING=(
        ('Не выбрано','Не выбрано'),
        ('Резко негативное','Резко негативное'),
        ('Негативное','ДНегативное'),
        ('Компромиссное','Компромиссное'),
        ('Помогу бросить курить','Помогу бросить курить'),
    )
    ATTITUDE_TO_ALCOHOL=(
        ('Не выбрано','Не выбрано'),
        ('Резко негативное','Резко негативное'),
        ('Негативное','ДНегативное'),
        ('Компромиссное','Компромиссное'),
        ('Помогу бросить пить','Помогу бросить пить'),
    )

    id = models.BigIntegerField(unique=True, primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="uuid")
    title = models.CharField(max_length=200, verbose_name="Название")
    activity = models.TextField(max_length=1000, verbose_name="Деятельность")
    interests = models.TextField(max_length=1000, verbose_name="Интересы")
    favorite_music = models.TextField(max_length=1000, verbose_name="Любимая музыка")
    favorite_films = models.TextField(max_length=1000, verbose_name="Любимые фильмы")
    favorite_books = models.TextField(max_length=1000, verbose_name="Любимые книги")
    about = models.TextField(max_length=1000, verbose_name="О себе")
    political_preferences = models.CharField(max_length=50, choices = POLITIC, verbose_name="Полит. предпочтения")
    worldview = models.CharField(max_length=50, choices = WORLDVIEW, verbose_name="Мировоззрение")
    mainthing_in_life = models.CharField(max_length=50, choices = MAINTHING_IN_LIFE, verbose_name="Главное в жизни")
    mainthing_in_people = models.CharField(max_length=50, choices = MAINTHING_IN_PEOPLE, verbose_name="Главное в людях")
    attitude_to_smoking = models.CharField(max_length=50, choices = ATTITUDE_TO_SMOKING, verbose_name="Отношение к курению")
    attitude_to_alcohol = models.CharField(max_length=50, choices = ATTITUDE_TO_ALCOHOL, verbose_name="Отношение к алкоголю")
    inspiration = models.CharField(max_length=200, verbose_name="Что меня вдохновляет")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Город")
    image = ProcessedImageField(format='JPEG', options={'quality': 90}, upload_to=upload_to_user_directory, processors=[ResizeToFit(width=1024, upscale=False)])
    is_active = models.BooleanField(default=False, verbose_name='Анкета активна')
    is_deleted = models.BooleanField(default=False, verbose_name='Анкета удалена')

    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Время публикации")
    is_reklama = models.BooleanField(default=False, verbose_name='Это реклама')
    votes_off = models.BooleanField(default=False, verbose_name='Лайки-дизлайки отключены')

    def __str__(self):
        return self.title

    class Meta:
        indexes = (BrinIndex(fields=['created']),)
        verbose_name = "Анкета"
        verbose_name_plural = "Анкеты"
        ordering=["-created"]

    def all_visits_count(self):
        from stst.models import AnketaNumbers

        return AnketaNumbers.objects.filter(anketa=self.pk).values('pk').count()

    def likes(self):
        from common.model.votes import AnketaVotes
        likes = AnketaVotes.objects.filter(parent=self, vote__gt=0)
        return likes

    def dislikes(self):
        from common.model.votes import AnketaVotes
        dislikes = AnketaVotes.objects.filter(parent=self, vote__lt=0)
        return dislikes


class AnketaFavourites(models.Model):
    anketa = models.ForeignKey(Anketa, on_delete=models.CASCADE, verbose_name="Анкета")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='anketa_favorites', on_delete=models.CASCADE, verbose_name="Пользователь")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Дата добавления")

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Избранная анкета"
        verbose_name_plural = "Избранные анкеты"
        unique_together = ('anketa', 'user',)
        indexes = (BrinIndex(fields=['created']),)
