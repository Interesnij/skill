from django.views.generic.base import TemplateView


class FaqView(TemplateView):
    template_name = "faq.html"
