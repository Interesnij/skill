from django.conf.urls import url
from users.view.manage import (
                                GetAdManage,
                                #GetSkillManage,
                                #GetAnketsManage,
                                #GetStaffManage,
                            )
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^module/(?P<pk>\d+)/$', login_required(GetAdManage.as_view()), name="get_module_staff")
    #url(r'^skill/(?P<pk>\d+)/$', login_required(GetSkillManage.as_view()), name="get_skill_staff"),
    #url(r'^ankets/(?P<pk>\d+)/$', login_required(GetAnketsManage.as_view()), name="get_ankets_staff"),
    #url(r'^staff/(?P<pk>\d+)/$', login_required(GetStaffManage.as_view()), name="get_users_staff"),
]
