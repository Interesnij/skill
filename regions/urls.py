from django.conf.urls import url
from regions.views import RegionView


urlpatterns = [
    url(r'^(?P<region_name>[\w\-]+)/$', RegionView.as_view(), name='region'),
]
