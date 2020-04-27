from django.db import models


class Country(models.Model):
	name_ru = models.CharField(max_length=100, verbose_name="Русское название")
	name_en = models.CharField(max_length=100, unique=True, verbose_name="Латинское название")
	order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер")
	image = models.ImageField(blank=True, verbose_name="Изображение", upload_to="countries")

	def __str__(self):
		return self.name_ru

	class Meta:
		verbose_name = "Страна"
		verbose_name_plural = "Страны"
