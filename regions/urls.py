from django.conf.urls import url
from regions.views import RegionView, AdsRegionView, CoursesRegionView, AnketsRegionView


urlpatterns = [
    url(r'^(?P<region_name>[\w\-]+)/$', RegionView.as_view(), name='region'),

    url(r'^ads/(?P<region_name>[\w\-]+)/$', AdsRegionView.as_view(), name="ads_region"),
	url(r'^courses/(?P<region_name>[\w\-]+)/$', CoursesRegionView.as_view(), name="courses_region"),
	url(r'^ankets/(?P<region_name>[\w\-]+)/$', AnketsRegionView.as_view(), name="ankets_region"),
]
