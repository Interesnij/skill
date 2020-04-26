from django.conf.urls import url
from skill_categories.views import (SkillCategoriesView,
                                    SkillCategoryView,
                                    SkillSubCategoryView,
                                    SkillRegionCategoryView,
                                    SkillCityCategoryView,
                                    SkillRegionSubCategoryView,
                                    SkillCitySubCategoryView,)


urlpatterns = [
    url(r'^$', SkillCategoriesView.as_view(), name='skill_categories'),
    url(r'^(?P<cat_name>[\w\-]+)/$', SkillCategoryView.as_view(), name='skill_category'),
    url(r'^subcat/(?P<subcat_name>[\w\-]+)/$', SkillSubCategoryView.as_view(), name='skill_subcategory'),

    url(r'^region_(?P<region_name>[\w\-]+)/(?P<cat_name>[\w\-]+)/$', SkillRegionCategoryView.as_view(), name='skill_category_region'),
    url(r'^sity_(?P<city_name>[\w\-]+)/(?P<cat_name>[\w\-]+)/$', SkillCityCategoryView.as_view(), name='skill_category_city'),

    url(r'^reg_(?P<region_name>[\w\-]+)/name_(?P<subcat_name>[\w\-]+)/$', SkillRegionSubCategoryView.as_view(), name='skill_subcategory_region'),
    url(r'^(?P<city_name>[\w\-]+)/sub_(?P<subcat_name>[\w\-]+)/$', SkillCitySubCategoryView.as_view(), name='skill_subcategory_city')
]
