from django.conf.urls import url
from countries.views import CountriesView, GetRegionsView


urlpatterns = [
    url(r'^$', CountriesView.as_view(), name='countries'),
    url(r'^load/(?P<pk>\d+)/$', GetRegionsView.as_view()),
]
