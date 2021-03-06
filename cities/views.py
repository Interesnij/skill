import re
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from regions.models import Region
from cities.models import City


class CityView(TemplateView):
	template_name = None

	def get(self,request,*args,**kwargs):
		from common.get_templates import get_template

		self.city = City.objects.get(name_en=self.kwargs["city_name"])
		self.template_name = get_template(folder="cities/", template="city.html", request=request)
		return super(CityView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super(CityView, self).get_context_data(**kwargs)
		context['last_ads'] = self.city.get_last_ads()
		context['last_courses'] = self.city.get_last_courses()
		context['last_ankets'] = self.city.get_last_ankets()
		context['city'] = self.city
		return context


class AdCityView(ListView):
	from ad_posts.models import Ad

	template_name = None
	model = Ad
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		from common.get_templates import get_ads_template

		self.city = City.objects.get(name_en=self.kwargs["city_name"])
		self.template_name = get_ads_template(folder="cities/ads/", template="ads.html", request=request)
		return super(AdCityView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		from ad_categories.models import AdCategory

		context = super(AdCityView, self).get_context_data(**kwargs)
		context['city'] = self.city
		context['ad_categories'] = AdCategory.objects.only("pk")
		return context
	def get_queryset(self):
		ads = self.city.get_ads()
		return ads


class CoursesCityView(ListView):
	from skill_posts.models import Course

	template_name = None
	model = Course
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		from common.get_templates import get_skills_template

		self.city = City.objects.get(name_en=self.kwargs["city_name"])
		self.template_name = get_skills_template(folder="cities/courses/", template="courses.html", request=request)
		return super(CoursesCityView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		from skill_categories.models import SkillCategory

		context = super(CoursesCityView, self).get_context_data(**kwargs)
		context['city'] = self.city
		context['skill_categories'] = SkillCategory.objects.only("pk")
		return context

	def get_queryset(self):
		courses = self.city.get_courses()
		return courses


class AnketsCityView(ListView):
	from love_posts.models import Anketa

	template_name = None
	model = Anketa
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		from common.get_templates import get_ankets_template

		self.city = City.objects.get(name_en=self.kwargs["city_name"])
		self.template_name = get_ankets_template(folder="cities/ankets/", template="ankets.html", request=request)
		return super(AnketsCityView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super(AnketsCityView, self).get_context_data(**kwargs)
		context['city'] = self.city
		return context

	def get_queryset(self):
		ankets = self.city.get_ankets()
		return ankets


class GetCitiesView(TemplateView):
    template_name = "get_cities.html"

    def get(self,request,*args,**kwargs):
        self.region = Region.objects.get(pk=self.kwargs["pk"])
        self.cities = City.objects.filter(region=self.region)
        return super(GetCitiesView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(GetCitiesView, self).get_context_data(**kwargs)
        context['cities'] = self.cities
        return context
