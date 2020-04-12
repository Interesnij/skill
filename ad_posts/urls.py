from django.conf.urls import url
from ad_posts.views import AdPostsView


urlpatterns = [
    url(r'^$', AdPostsView.as_view(), name='ad_posts'),
]
