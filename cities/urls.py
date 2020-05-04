from django.conf.urls import url
from cities.views import CityView, GetCitiesView, AdCitiesView, CoursesCitiesView, AnketsCitiesView


urlpatterns = [
    url(r'^(?P<city_name>[\w\-]+)/$', CityView.as_view(), name='city'),
    url(r'^load/(?P<pk>\d+)/$', GetCitiesView.as_view()),

    url(r'^ads/(?P<region_name>[\w\-]+)/$', AdCitiesView.as_view(), name="ads_city"),
	url(r'^courses/(?P<city_name>[\w\-]+)/$', CoursesCitiesView.as_view(), name="courses_city"),
	url(r'^ankets/(?P<city_name>[\w\-]+)/$', AnketsCitiesView.as_view(), name="ankets_city"),
]
