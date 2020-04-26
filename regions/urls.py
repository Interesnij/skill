from django.conf.urls import url
from regions.views import RegionView, RegionCategoryView, RegionSubCategoryView


urlpatterns = [
    url(r'^(?P<region_name>[\w\-]+)/$', RegionView.as_view(), name='region'),
    url(r'^cat/(?P<region_name>[\w\-]+)/(?P<cat_name>[\w\-]+)/$', RegionCategoryView.as_view(), name='category_region'),
    url(r'^subcat/(?P<region_name>[\w\-]+)/name_(?P<subcat_name>[\w\-]+)/$', RegionSubCategoryView.as_view(), name='subcategory_region'),
]
