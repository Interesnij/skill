import re
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from regions.models import Region


class RegionView(TemplateView):
	template_name = None

	def get(self,request,*args,**kwargs):
		from common.get_templates import get_template

		self.region = Region.objects.get(name_en=self.kwargs["region_name"])
		self.template_name = get_template(folder="region/", template="region.html", request=request)

		return super(RegionView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super(RegionView, self).get_context_data(**kwargs)
		context['last_ads'] = self.region.get_last_ads()
		context['last_courses'] = self.region.get_last_courses()
		context['last_ankets'] = self.region.get_last_ankets()
		context['region'] = self.region
		return context


class AdsRegionView(ListView):
	from ad_posts.models import Ad

	template_name = None
	model = Ad
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		from common.get_templates import get_ads_template

		self.region = Region.objects.get(name_en=self.kwargs["region_name"])
		self.template_name = get_ads_template(folder="region/ads/", template="ads.html", request=request)
		return super(AdsRegionView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		from ad_categories.models import AdCategory

		context = super(AdsRegionView, self).get_context_data(**kwargs)
		context['region'] = self.region
		context['ad_categories'] = AdCategory.objects.only("pk")
		return context
	def get_queryset(self):
		ads = self.region.get_ads()
		return ads


class CoursesRegionView(ListView):
	from skill_posts.models import Course

	template_name = None
	model = Course
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		from common.get_templates import get_skills_template

		self.region = Region.objects.get(name_en=self.kwargs["region_name"])
		self.template_name = get_skills_template(folder="region/courses/", template="courses.html", request=request)
		return super(CoursesRegionView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		from skill_categories.models import SkillCategory

		context = super(CoursesRegionView, self).get_context_data(**kwargs)
		context['region'] = self.region
		context['skill_categories'] = SkillCategory.objects.only("pk")
		return context

	def get_queryset(self):
		courses = self.region.get_courses()
		return courses


class AnketsRegionView(ListView):
	from love_posts.models import Anketa

	template_name = None
	model = Anketa
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		from common.get_templates import get_ankets_template

		self.region = Region.objects.get(name_en=self.kwargs["region_name"])
		self.template_name = get_ankets_template(folder="region/ankets/", template="ankets.html", request=request)
		return super(AnketsRegionView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super(AnketsRegionView, self).get_context_data(**kwargs)
		context['region'] = self.region
		return context

	def get_queryset(self):
		ankets = self.region.get_ankets()
		return ankets
