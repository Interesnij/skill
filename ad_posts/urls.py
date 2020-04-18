from django.conf.urls import url
from ad_posts.views import AdPostsView, AdDetailView, AdCreate


urlpatterns = [
    url(r'^$', AdPostsView.as_view(), name='ad_posts'),
    url(r'^(?P<pk>\d+)/detail/$',AdDetailView.as_view(), name="ad_detail"),
    url(r'^add/$',AdCreate.as_view(), name="ad_add"),
]
