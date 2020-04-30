from django.conf.urls import url, include
from users.views import *


urlpatterns = [
    url(r'(?P<pk>\d+)/$', ProfileUserView.as_view(), name='user'),
    url(r'(?P<pk>\d+)/posts/$', UserAdsView.as_view(), name='user_ads'),
    url(r'courses/(?P<pk>\d+)/$', UserCoursesView.as_view(), name='my_courses'),
    url(r'(?P<pk>\d+)/ankets/$', UserAnketsView.as_view(), name='user_ankets'),
    url(r'(?P<pk>\d+)/my_favorites/$', UserFavoriteView.as_view(), name='user_favorite'),
    url(r'(?P<pk>\d+)/my_subscribe/$', MySubscribeView.as_view(), name='my_subscribes'),
    url(r'(?P<pk>\d+)/subscribes/$', SubscribesView.as_view(), name='subscribes'),
    url(r'(?P<pk>\d+)/settings/$', UserSettingsView.as_view(), name='user_settings'),

    url(r'progs/', include('users.url.progs')),
    url(r'ad_progs/', include('users.url.ad_progs')),

]
