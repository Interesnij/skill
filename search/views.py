from django.views.generic.base import TemplateView
from ad_categories.models import AdCategory, AdSubCategory


class SearchView(TemplateView):
    template_name = "search.html"


class GetSubCat(TemplateView):
    template_name = "get_subcat.html"

    def get(self,request,*args,**kwargs):
        self.cat = AdCategory.objects.get(pk=self.kwargs["pk"])
        self.subcats = AdSubCategory.objects.filter(category=self.cat)
        return super(GetSubCat,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(CityView, self).get_context_data(**kwargs)
        context['subcats'] = self.subcats
        return context
