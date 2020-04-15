from django.db import models
from regions.models import Region


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион")
    name_ru = models.CharField(max_length=100, verbose_name="Русское название")
    name_en = models.CharField(max_length=100, verbose_name="Латинское название")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер")
    image = models.ImageField(blank=True, verbose_name="Изображение", upload_to="cities")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
