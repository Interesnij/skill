from django.conf.urls import url
from countries.views import CountriesView


urlpatterns = [
    url(r'^$', CountriesView.as_view(), name='countries'),
]
