from django.views.generic.base import TemplateView


class MainPageView(TemplateView):
	template_name='main/test.html'

class TestPageView(TemplateView):
	template_name='main/test.html'
