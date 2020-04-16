from django.conf.urls import url, include
from users.views import *


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProfileUserView.as_view(), name='user'),
    url(r'^(?P<pk>\d+)/active/$', UserAdActiveView.as_view(), name='user_ad_active'),
    url(r'^(?P<pk>\d+)/sold/$', UserAdSoldView.as_view(), name='user_ad_sold'),
    url(r'^(?P<pk>\d+)/deferred/$', UserAdDefView.as_view(), name='user_ad_deferred'),
    url(r'^(?P<pk>\d+)/favorite/$', UserFavoriteView.as_view(), name='user_favorite'),
    url(r'^(?P<pk>\d+)/my_subscribe/$', MySubscribeView.as_view(), name='my_subscribe'),
    url(r'^(?P<pk>\d+)/subscribes/$', SubscribesView.as_view(), name='subscribes'),
    url(r'^(?P<pk>\d+)/settings/$', UserSettingsView.as_view(), name='user_settings'),

    url(r'^progs/', include('users.url.progs')),
    url(r'^ad_progs/', include('users.url.ad_progs')),

]
