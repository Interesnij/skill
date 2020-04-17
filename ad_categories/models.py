from django.db import models
from django.db.models import Q


class AdCategory(models.Model):
	name_ru = models.CharField(max_length=100, unique=True, verbose_name="Русское название")
	name_en = models.CharField(max_length=100, unique=True, verbose_name="Английское название")
	order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер")
	image = models.ImageField(blank=True, verbose_name="Изображение", upload_to="ad_category/cat")

	def __str__(self):
		return self.name_ru

	class Meta:
		verbose_name = "Категория объявлений"
		verbose_name_plural = "Категории объявлений"

	def last_ads(self):
	    from ad_posts.models import Ad

	    ads_query = Q(category__category__id=self.id, creator__is_blocked=False, is_deleted=False, is_active=True)
	    ads = Ad.objects.filter(ads_query)
	    return ads[:21]

	def get_ads(self):
	    from ad_posts.models import Ad

	    ads_query = Q(category__category__id=self.id, creator__is_blocked=False, is_deleted=False, is_active=True)
	    ads = Ad.objects.filter(ads_query)
	    return ads

	def get_ads_in_region(self, region_id):
	    from ad_posts.models import Ad

	    ads_query = Q(category__category__id=self.id, city__region__id=region_id, creator__is_blocked=False, is_deleted=False, is_active=True)
	    ads = Ad.objects.filter(ads_query)
	    return ads

	def get_ads_in_city(self, city_id):
	    from ad_posts.models import Ad

	    ads_query = Q(category__category__id=self.id, city__id=city_id, creator__is_blocked=False, is_deleted=False, is_active=True)
	    ads = Ad.objects.filter(ads_query)
	    return ads


class AdSubCategory(models.Model):
	category = models.ForeignKey(AdCategory, on_delete=models.CASCADE, verbose_name="Категория-родитель")
	name_ru = models.CharField(max_length=100, verbose_name="Название подкатегории")
	name_en = models.CharField(max_length=100, unique=True, verbose_name="Английское название")
	order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер подкатегории")
	image = models.ImageField(blank=True, verbose_name="Изображение", upload_to="ad_category/sub")

	def __str__(self):
		return self.name_ru

	class Meta:
		verbose_name = "суб-категория"
		verbose_name_plural = "суб-категории"

	def get_absolute_url(self):
		return reverse('subcategories_edit',kwargs={"pk":self.pk})


	def last_ads(self):
	    from ad_posts.models import Ad

	    ads_query = Q(category__id=self.id, creator__is_blocked=False, is_deleted=False, is_active=True)
	    ads = Ad.objects.filter(ads_query)
	    return ads[:21]

	def get_ads(self):
	    from ad_posts.models import Ad

	    ads_query = Q(category__id=self.id, creator__is_blocked=False, is_deleted=False, is_active=True)
	    ads = Ad.objects.filter(ads_query)
	    return ads

	def get_ads_in_region(self, region_id):
	    from ad_posts.models import Ad

	    ads_query = Q(category__id=self.id, city__region__id=region_id, creator__is_blocked=False, is_deleted=False, is_active=True)
	    ads = Ad.objects.filter(ads_query)
	    return ads

	def get_ads_in_city(self, city_id):
	    from ad_posts.models import Ad

	    ads_query = Q(category__id=self.id, city__id=city_id, creator__is_blocked=False, is_deleted=False, is_active=True)
	    ads = Ad.objects.filter(ads_query)
	    return ads
