import re
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from skill_categories.models import SkillCategory, SkillSubCategory
from skill_posts.models import Course
from regions.models import Region
from cities.models import City


class SkillCategoriesView(TemplateView):
    template_name = "skill_categories.html"


class SkillCategoryView(ListView):
    template_name = None
    model = Course
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.cat=SkillCategory.objects.get(name_en=self.kwargs["cat_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "skill_cat/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "skill_cat/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(SkillCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(SkillCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        context['skill_categories'] = SkillCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.cat.get_course()
        return ads


class SkillRegionCategoryView(ListView):
    template_name = None
    model = Course
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.cat=SkillCategory.objects.get(name_en=self.kwargs["cat_name"])
        self.region=Region.objects.get(name_en=self.kwargs["region_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "skill_cat_region/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "skill_cat_region/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(SkillRegionCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(SkillRegionCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        context['region'] = self.region
        context['skill_categories'] = SkillCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.cat.get_course_in_region(self.region.pk)
        return ads


class SkillCityCategoryView(ListView):
    template_name = None
    model = Course
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.cat=SkillCategory.objects.get(name_en=self.kwargs["cat_name"])
        self.city=City.objects.get(name_en=self.kwargs["city_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "skill_cat_city/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "skill_cat_city/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(SkillCityCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(SkillCityCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        context['city'] = self.city
        return context

    def get_queryset(self):
        ads = self.cat.get_course_in_city(self.city.pk)
        return ads


class SkillSubCategoryView(ListView):
    template_name = None
    model = Course
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.cat=SkillSubCategory.objects.get(name_en=self.kwargs["subcat_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "skill_subcat/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "skill_subcat/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(SkillSubCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(SkillSubCategoryView, self).get_context_data(**kwargs)
        context['sub_category'] = self.cat
        context['skill_categories'] = SkillCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.cat.get_course()
        return ads


class SkillRegionSubCategoryView(ListView):
    template_name = None
    model = Course
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.cat=SkillSubCategory.objects.get(name_en=self.kwargs["subcat_name"])
        self.region=Region.objects.get(name_en=self.kwargs["region_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "skill_subcat_region/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "skill_subcat_region/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(SkillRegionSubCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(SkillRegionSubCategoryView, self).get_context_data(**kwargs)
        context['sub_category'] = self.cat
        context['region'] = self.region
        context['skill_categories'] = SkillCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.cat.get_course_in_region(self.region.pk)
        return ads


class SkillCitySubCategoryView(ListView):
    template_name = None
    model = Course
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.cat=SkillSubCategory.objects.get(name_en=self.kwargs["subcat_name"])
        self.city=City.objects.get(name_en=self.kwargs["city_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "skill_subcat_city/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "skill_subcat_city/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(SkillCitySubCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(SkillCitySubCategoryView, self).get_context_data(**kwargs)
        context['sub_category'] = self.cat
        context['city'] = self.city
        context['skill_categories'] = SkillCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.cat.get_course_in_city(self.city.pk)
        return ads
