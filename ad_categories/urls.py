from django.conf.urls import url
from ad_categories.views import AdCategoriesView


urlpatterns = [
    url(r'^$', AdCategoriesView.as_view(), name='ad_categories'),
]
