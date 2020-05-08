from django.conf.urls import url
from ad_posts.view.votes import AdLike, AdDisLike
from django.contrib.auth.decorators import login_required


urlpatterns = [
	url(r'^like/(?P<uuid>[0-9a-f-]+)/(?P<pk>\d+)/$',login_required(AdLike.as_view())),
    url(r'^dislike/(?P<uuid>[0-9a-f-]+)/(?P<pk>\d+)/$',login_required(AdDisLike.as_view())),
]
