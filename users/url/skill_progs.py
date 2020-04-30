from django.conf.urls import url
from users.view.skill_progs import SkillActive, SkillUnActive, SkillDelete, SkillUnDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^active/(?P<pk>\d+)/$', login_required(SkillActive.as_view())),
    url(r'^unactive/(?P<pk>\d+)/$', login_required(SkillUnActive.as_view())),
    url(r'^delete/(?P<pk>\d+)/$', login_required(SkillDelete.as_view())),
    url(r'^undelete/(?P<pk>\d+)/$', login_required(SkillUnDelete.as_view())),
]
