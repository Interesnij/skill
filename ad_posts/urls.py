from django.conf.urls import url, include
from ad_posts.views import AdPostsView, AdDetailView, AdCreate, FormAdd


urlpatterns = [
    url(r'^$', AdPostsView.as_view(), name='ad_posts'),
    url(r'^(?P<pk>\d+)/detail/$',AdDetailView.as_view(), name="ad_detail"),
    url(r'^add/$',AdCreate.as_view(), name="ad_add"),
    url(r'^form_special/(?P<pk>\d+)/$', FormAdd.as_view()),

    url(r'^votes/', include('ad_posts.url.votes')),
]
