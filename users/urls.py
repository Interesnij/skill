from django.conf.urls import url, include
from users.views import ProfileUserView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProfileUserView.as_view(), name='user'),

    url(r'^progs/', include('users.url.progs')),

]
