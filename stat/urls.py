from django.conf.urls import url
from stat.views import StatView, StatAdView


urlpatterns = [
    url(r'^$', StatView.as_view(), name='stat'),
    url(r'^ad/(?P<uuid>[0-9a-f-]+)/$', StatAdView.as_view(), name='stat_ad'),
]
