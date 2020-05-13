from django.views.generic.base import TemplateView


class LogsView(TemplateView):
    template_name = "logs.html"
