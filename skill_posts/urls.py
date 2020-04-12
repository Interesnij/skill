from django.conf.urls import url
from skill_posts.views import SkillPostsView


urlpatterns = [
    url(r'^$', SkillPostsView.as_view(), name='skill_posts'),
]
