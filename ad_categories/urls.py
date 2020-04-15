from django.conf.urls import url
from ad_categories.views import *


urlpatterns = [
    url(r'^$', AdCategoriesView.as_view(), name='ad_categories'),

    url(r'^(?P<cat_name>[\w\-]+)/$', AdCategoryView.as_view(), name='ad_category'),
    url(r'^region_(?P<region_name>[\w\-]+)/(?P<cat_name>[\w\-]+)/$', AdRegionCategoryView.as_view(), name='ad_category_region'),
    url(r'^sity_(?P<city_name>[\w\-]+)/(?P<cat_name>[\w\-]+)/$', AdCityCategoryView.as_view(), name='ad_category_city'),

    url(r'^sub_(?P<subcat_name>[\w\-]+)/$', AdSubCategoryView.as_view(), name='ad_subcategory'),
    url(r'^reg_(?P<region_name>[\w\-]+)/name_(?P<subcat_name>[\w\-]+)/$', AdRegionSubCategoryView.as_view(), name='ad_subcategory_region'),
    url(r'^sity_(?P<city_name>[\w\-]+)/sub_(?P<subcat_name>[\w\-]+)/$', AdCitySubCategoryView.as_view(), name='ad_subcategory_city'),
]
