from django.conf.urls import url
from skill_categories.views import SkillCategoriesView, SkillCategoryView


urlpatterns = [
    url(r'^$', SkillCategoriesView.as_view(), name='skill_categories'),
    url(r'^(?P<cat_name>[\w\-]+)/$', SkillCategoryView.as_view(), name='skill_category'),
]
