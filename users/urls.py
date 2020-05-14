from django.conf.urls import url, include
from users.views import *


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProfileUserView.as_view(), name='user'),
    url(r'^posts/(?P<pk>\d+)/$', UserAdsView.as_view(), name='user_ads'),
    url(r'^courses/(?P<pk>\d+)/$', UserCoursesView.as_view(), name='my_courses'),
    url(r'^ankets/(?P<pk>\d+)/$', UserAnketsView.as_view(), name='user_ankets'),
    url(r'^blacklist/(?P<pk>\d+)/$', UserBlackListView.as_view(), name='user_blacklist'),
    url(r'^my_favorites/(?P<pk>\d+)/$', UserFavoriteView.as_view(), name='user_favorite'),
    url(r'^my_subscribe/(?P<pk>\d+)/$', MySubscribeView.as_view(), name='my_subscribes'),
    url(r'^subscribes/(?P<pk>\d+)/$', SubscribesView.as_view(), name='subscribes'),
    url(r'^settings/(?P<pk>\d+)/$', UserSettingsView.as_view(), name='user_settings'),

    url(r'^progs/', include('users.url.progs')),
    url(r'^ad_progs/', include('users.url.ad_progs')),
    url(r'^skill_progs/', include('users.url.skill_progs')),
    url(r'^love_progs/', include('users.url.love_progs')),
    url(r'^manage/', include('users.url.manage')),
]
