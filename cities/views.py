from django.views.generic.base import TemplateView


class CitiesView(TemplateView):
    template_name = "cities.html"
