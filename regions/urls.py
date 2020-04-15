from django.conf.urls import url
from regions.views import RegionView


urlpatterns = [
    url(r'(?P<region>[\w\-]+)/^$', RegionView.as_view(), name='region'),
]
