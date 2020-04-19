from django.conf.urls import url
from cities.views import CityView, GetCitiesView


urlpatterns = [
    url(r'^(?P<city_name>[\w\-]+)/$', CityView.as_view(), name='city'),
    url(r'^load/(?P<pk>\d+)/$', GetCitiesView.as_view()),
]
