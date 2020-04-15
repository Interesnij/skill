from django.conf.urls import url
from cities.views import CityView


urlpatterns = [
    url(r'(?P<city_name>[\w\-]+)/$', CityView.as_view(), name='city'),
]
