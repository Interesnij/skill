from django.db import models
from django.contrib.postgres.indexes import BrinIndex


class Quan(models.Model):
	question = models.CharField(max_length=200, verbose_name="Вопрос")
	answer = models.TextField(verbose_name="Ответ")
	created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Время публикации")

	def __str__(self):
		return self.question

	class Meta:
		verbose_name = "Вопросы-ответы"
		verbose_name_plural = "Вопросы-ответы"
		ordering = ['-created']
		indexes = (BrinIndex(fields=['created']),)
