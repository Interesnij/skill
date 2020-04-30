from django.conf.urls import url
from users.view.love_progs import AnketaActive, AnketaUnActive, AnketaDelete, AnketaUnDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^active/(?P<pk>\d+)/$', login_required(AnketaActive.as_view())),
    url(r'^unactive/(?P<pk>\d+)/$', login_required(AnketaUnActive.as_view())),
    url(r'^delete/(?P<pk>\d+)/$', login_required(AnketaDelete.as_view())),
    url(r'^undelete/(?P<pk>\d+)/$', login_required(AnketaUnDelete.as_view())),
]