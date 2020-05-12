import re
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from ad_categories.models import AdCategory, AdSubCategory
from ad_posts.models import Ad
from regions.models import Region
from cities.models import City


class AdCategoriesView(TemplateView):
    template_name = "ad_categories.html"


class AdCategoryView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        from common.get_templates import get_ads_template

        self.cat=AdCategory.objects.get(name_en=self.kwargs["cat_name"])
        self.template_name = get_ads_template(folder="ad_cat/", template="page.html", request=request)
        return super(AdCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        context['ad_categories'] = AdCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.cat.get_ads()
        return ads


class AdRegionCategoryView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        from common.get_templates import get_ads_template

        self.cat=AdCategory.objects.get(name_en=self.kwargs["cat_name"])
        self.region=Region.objects.get(name_en=self.kwargs["region_name"])
        self.template_name = get_ads_template(folder="ad_cat_region/", template="page.html", request=request)
        return super(AdRegionCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdRegionCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        context['region'] = self.region
        context['ad_categories'] = AdCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.cat.get_ads_in_region(self.region.pk)
        return ads


class AdCityCategoryView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        from common.get_templates import get_ads_template

        self.cat=AdCategory.objects.get(name_en=self.kwargs["cat_name"])
        self.city=City.objects.get(name_en=self.kwargs["city_name"])
        self.template_name = get_ads_template(folder="ad_cat_city/", template="page.html", request=request)
        return super(AdCityCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdCityCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        context['city'] = self.city
        return context

    def get_queryset(self):
        ads = self.cat.get_ads_in_city(self.city.pk)
        return ads


class AdSubCategoryView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        from common.get_templates import get_ads_template

        self.cat=AdSubCategory.objects.get(name_en=self.kwargs["subcat_name"])
        self.template_name = get_ads_template(folder="ad_subcat/", template="page.html", request=request)
        return super(AdSubCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdSubCategoryView, self).get_context_data(**kwargs)
        context['sub_category'] = self.cat
        context['ad_categories'] = AdCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.cat.get_ads()
        return ads


class AdRegionSubCategoryView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        from common.get_templates import get_ads_template

        self.cat=AdSubCategory.objects.get(name_en=self.kwargs["subcat_name"])
        self.region=Region.objects.get(name_en=self.kwargs["region_name"])
        self.template_name = get_ads_template(folder="ad_subcat_region/", template="page.html", request=request)
        return super(AdRegionSubCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdRegionSubCategoryView, self).get_context_data(**kwargs)
        context['sub_category'] = self.cat
        context['region'] = self.region
        context['ad_categories'] = AdCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.cat.get_ads_in_region(self.region.pk)
        return ads


class AdCitySubCategoryView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        from common.get_templates import get_ads_template

        self.cat=AdSubCategory.objects.get(name_en=self.kwargs["subcat_name"])
        self.city=City.objects.get(name_en=self.kwargs["city_name"])
        self.template_name = get_ads_template(folder="ad_subcat_city/", template="page.html", request=request)
        return super(AdCitySubCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdCitySubCategoryView, self).get_context_data(**kwargs)
        context['sub_category'] = self.cat
        context['city'] = self.city
        context['ad_categories'] = AdCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.cat.get_ads_in_city(self.city.pk)
        return ads
