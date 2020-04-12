from django.views.generic.base import TemplateView


class CountriesView(TemplateView):
    template_name = "countries.html"
