from django.conf.urls import url
from ad_categories.views import AdCategoriesView, AdCategoryView, AdSubCategoryView


urlpatterns = [
    url(r'^$', AdCategoriesView.as_view(), name='ad_categories'),
    url(r'^cat/(?P<name_en>[\w\-]+)/$', AdCategoryView.as_view(), name='ad_category'),
    url(r'^sub_cat/(?P<name_en>[\w\-]+)/$', AdSubCategoryView.as_view(), name='ad_subcategory'),
]
