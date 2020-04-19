from django.views.generic.base import TemplateView
from django.views.generic import ListView
from cities.models import City
from regions.models import Region
from ad_posts.models import Ad
import re
from ad_categories.models import AdCategory


class CityView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.city = City.objects.get(name_en=self.kwargs["city_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "city/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "city/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(CityView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(CityView, self).get_context_data(**kwargs)
        context['city'] = self.city
        context['ad_categories'] = AdCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.city.get_ads()
        return ads


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
