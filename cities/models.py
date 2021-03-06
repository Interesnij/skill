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
        ordering = ["order"]

    def __str__(self):
        return self.name_ru

    def get_ads(self):
	    from ad_posts.models import Ad

	    ads_query = Q(city__id=self.id, creator__is_blocked=False, is_deleted=False, is_active=True)
	    ads = Ad.objects.filter(ads_query)
	    return ads

    def get_last_ads(self):
	    from ad_posts.models import Ad

	    ads_query = Q(city__id=self.id, creator__is_blocked=False, is_deleted=False, is_active=True)
	    ads = Ad.objects.filter(ads_query)
	    return ads[0:21]

    def get_courses(self):
        from skill_posts.models import Course

        courses_query = Q(city__id=self.id, creator__is_blocked=False, is_private=False, is_deleted=False, is_active=True)
        courses = Course.objects.filter(courses_query)
        return courses

    def get_last_courses(self):
        from skill_posts.models import Course

        courses_query = Q(city__id=self.id, creator__is_blocked=False, is_private=False, is_deleted=False, is_active=True)
        courses = Course.objects.filter(courses_query)
        return courses[0:21]

    def get_ankets(self):
        from love_posts.models import Anketa

        ankets_query = Q(city__id=self.id, creator__is_blocked=False, is_deleted=False, is_active=True)
        ankets = Anketa.objects.filter(ankets_query)
        return ankets

    def get_last_ankets(self):
        from love_posts.models import Anketa

        ankets_query = Q(city__id=self.id, creator__is_blocked=False, is_deleted=False, is_active=True)
        ankets = Anketa.objects.filter(ankets_query)
        return ankets[0:21]
