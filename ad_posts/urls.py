from django.conf.urls import url
from ad_posts.views import AdPostsView, AdDetailView


urlpatterns = [
    url(r'^$', AdPostsView.as_view(), name='ad_posts'),
    url(r'^(?P<pk>\d+)/detail/$',AdDetailView.as_view(), name="ad_detail"),
]
