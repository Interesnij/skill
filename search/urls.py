from django.conf.urls import url
from search.views import SearchView, GetSubCat


urlpatterns = [
    url(r'^$', SearchView.as_view(), name='search'),
    url(r'get_subcat/(?P<pk>\d+)/$', GetSubCat.as_view()),
]
