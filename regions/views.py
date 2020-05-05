import re
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from regions.models import Region


class RegionView(TemplateView):
	template_name = None

	def get(self,request,*args,**kwargs):
		import re

		self.region = Region.objects.get(name_en=self.kwargs["region_name"])
		if request.user.is_authenticated and not request.user.is_deleted:
			self.template_name = "region/region.html"
		elif request.user.is_authenticated and request.user.is_deleted:
			self.template_name = "generic/user_deleted.html"
		elif request.user.is_anonymous:
			self.template_name = "region/anon_region.html"

		MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
		if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
			self.template_name = "mob_" + self.template_name
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
		self.region = Region.objects.get(name_en=self.kwargs["region_name"])
		if request.user.is_authenticated and not request.user.is_deleted:
			self.template_name = "region/ads.html"
		elif request.user.is_authenticated and request.user.is_deleted:
			self.template_name = "generic/user_deleted.html"
		elif request.user.is_anonymous:
			self.template_name = "region/anon_ads.html"

		MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
		if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
			self.template_name = "mob_" + self.template_name
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
		self.region = Region.objects.get(name_en=self.kwargs["region_name"])
		if request.user.is_authenticated and not request.user.is_deleted:
			self.template_name = "region/courses.html"
		elif request.user.is_authenticated and request.user.is_deleted:
			self.template_name = "generic/user_deleted.html"
		elif request.user.is_anonymous:
			self.template_name = "region/anon_courses.html"

		MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
		if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
			self.template_name = "mob_" + self.template_name
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
		self.region = Region.objects.get(name_en=self.kwargs["region_name"])
		if request.user.is_authenticated and not request.user.is_deleted:
			self.template_name = "region/ankets.html"
		elif request.user.is_authenticated and request.user.is_deleted:
			self.template_name = "generic/user_deleted.html"
		elif request.user.is_anonymous:
			self.template_name = "region/anon_ankets.html"

		MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
		if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
			self.template_name = "mob_" + self.template_name
		return super(AnketsRegionView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super(AnketsRegionView, self).get_context_data(**kwargs)
		context['region'] = self.region
		return context

	def get_queryset(self):
		ankets = self.region.get_ankets()
		return ankets
