from django.views.generic.base import TemplateView


class NewsView(TemplateView):
    template_name = "news.html"
