from django.conf.urls import url
from news.views import NewsView


urlpatterns = [
    url(r'^$', NewsView.as_view(), name='news'),
]
