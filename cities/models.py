from django.db import models
from regions.models import Region
from django.db.models import Q


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион")
    name_ru = models.CharField(max_length=100, verbose_name="Русское название")
    name_en = models.CharField(max_length=100, unique=True, verbose_name="Латинское название")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер")
    image = models.ImageField(blank=True, verbose_name="Изображение", upload_to="cities")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name_ru

    def get_ads(self):
	    from ad_posts.models import Ad

	    ads_query = Q(city__id=self.id, creator__is_blocked=False, is_deleted=False, is_active=True)
	    ads = Ad.objects.filter(ads_query)
	    return ads
