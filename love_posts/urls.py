from django.conf.urls import url
from love_posts.views import LovePostsView, AnketaDetailView, AnketaCreate


urlpatterns = [
    url(r'^$', LovePostsView.as_view(), name='love_posts'),
    url(r'^(?P<pk>\d+)/detail/$',AnketaDetailView.as_view(), name="anketa_detail"),
    url(r'^add/$',AnketaCreate.as_view(), name="anketa_add"),
]
