from django.conf.urls import url
from users.view.ad_progs import AdSold, AdUnSold, AdActive, AdUnActive, AdDelete, AdUnDelete, AdFavorite, AdUnFavorite
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^sold/(?P<pk>\d+)/$', login_required(AdSold.as_view())),
    url(r'^unsold/(?P<pk>\d+)/$', login_required(AdUnSold.as_view())),
    url(r'^active/(?P<pk>\d+)/$', login_required(AdActive.as_view())),
    url(r'^unactive/(?P<pk>\d+)/$', login_required(AdUnActive.as_view())),
    url(r'^delete/(?P<pk>\d+)/$', login_required(AdDelete.as_view())),
    url(r'^undelete/(?P<pk>\d+)/$', login_required(AdUnDelete.as_view())),

    url(r'^favorite/(?P<pk>\d+)/$', login_required(AdFavorite.as_view())),
    url(r'^unfavorite/(?P<pk>\d+)/$', login_required(AdUnFavorite.as_view())),
]
