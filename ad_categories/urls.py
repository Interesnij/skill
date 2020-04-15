from django.conf.urls import url
from ad_categories.views import *


urlpatterns = [
    url(r'^$', AdCategoriesView.as_view(), name='ad_categories'),

    url(r'(?P<cat_name>[\w\-]+)/$', AdCategoryView.as_view(), name='ad_category'),
    url(r'(?P<cat_name>[\w\-]+)/region/(?P<region_name>[\w\-]+)/$', AdRegionCategoryView.as_view(), name='ad_category_region'),
    url(r'(?P<cat_name>[\w\-]+)/city/(?P<city_name>[\w\-]+)/$', AdCityCategoryView.as_view(), name='ad_category_city'),

    url(r'sub_cat/(?P<subcat_name>[\w\-]+)/$', AdSubCategoryView.as_view(), name='ad_subcategory'),
    url(r'sub_region/(?P<region_name>[\w\-]+)/(?P<subcat_name>[\w\-]+)/$', AdRegionSubCategoryView.as_view(), name='ad_subcategory_region'),
    url(r'sub_city/(?P<city_name>[\w\-]+)/(?P<subcat_name>[\w\-]+)/$', AdCitySubCategoryView.as_view(), name='ad_subcategory_city'),
]
