from django.conf.urls import url
from ad_categories.views import AdCategoriesView, AdCategoryView, AdSubCategoryView


urlpatterns = [
    url(r'^$', AdCategoriesView.as_view(), name='ad_categories'),
    url(r'^cat/(?P<cat_name>[\w\-]+)/$', AdCategoryView.as_view(), name='ad_category'),
    url(r'^sub_cat/(?P<subcat_name>[\w\-]+)/$', AdSubCategoryView.as_view(), name='ad_subcategory'),
]
