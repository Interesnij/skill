from django.conf.urls import url
from skill_posts.views import SkillPostsView, CourseDetailView, CourseCreate


urlpatterns = [
    url(r'^$', SkillPostsView.as_view(), name='skill_posts'),
    url(r'^(?P<pk>\d+)/detail/$',CourseDetailView.as_view(), name="course_detail"),
    url(r'^add/$',CourseCreate.as_view(), name="course_add"),
]
