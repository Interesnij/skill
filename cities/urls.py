from django.conf.urls import url
from cities.views import CitiesView


urlpatterns = [
    url(r'^$', CitiesView.as_view(), name='cities'),
]
