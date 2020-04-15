from django.views.generic.base import TemplateView
from countries.models import Country
from regions.models import Region


class CountriesView(TemplateView):
    template_name = "countries.html"


class GetRegionsView(TemplateView):
    template_name = "get_regions.html"

    def get(self,request,*args,**kwargs):
        self.country = Country.objects.get(pk=self.kwargs["pk"])
        self.regions = Region.objects.filter(country=self.country)
        return super(GetRegionsView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(GetRegionsView, self).get_context_data(**kwargs)
        context['country'] = self.country
        context['regions'] = self.regions
        return context
