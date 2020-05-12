from django.conf.urls import url
from users.view.skill_progs import (
                                    SkillActive,
                                    SkillUnActive,
                                    SkillDelete,
                                    SkillUnDelete,

                                    SkillFavorite,
                                    SkillUnFavorite,

                                    SkillAdminCreate,
                                    SkillAdminDelete,
                                    SkillModerCreate,
                                    SkillModerDelete,
                                    SkillEditorCreate,
                                    SkillEditorDelete,
                                    SkillAdvertiserCreate,
                                    SkillAdvertiserDelete,
                                    SkillTeacherCreate,
                                    SkillTeacherDelete,

                                    SkillWorkerAdminCreate,
                                    SkillWorkerAdminDelete,
                                    SkillWorkerModerCreate,
                                    SkillWorkerModerDelete,
                                    SkillWorkerEditorCreate,
                                    SkillWorkerEditorDelete,
                                    SkillWorkerAdvertiserCreate,
                                    SkillWorkerAdvertiserDelete,
                                    SkillWorkerTeacherCreate,
                                    SkillWorkerTeacherDelete
                                    )
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^active/(?P<pk>\d+)/$', login_required(SkillActive.as_view())),
    url(r'^unactive/(?P<pk>\d+)/$', login_required(SkillUnActive.as_view())),
    url(r'^delete/(?P<pk>\d+)/$', login_required(SkillDelete.as_view())),
    url(r'^undelete/(?P<pk>\d+)/$', login_required(SkillUnDelete.as_view())),

    url(r'^favorite/(?P<pk>\d+)/$', login_required(SkillFavorite.as_view())),
    url(r'^unfavorite/(?P<pk>\d+)/$', login_required(SkillUnFavorite.as_view())),

    url(r'^add_admin/(?P<pk>\d+)/$', login_required(SkillAdminCreate.as_view())),
    url(r'^delete_admin/(?P<pk>\d+)/$', login_required(SkillAdminDelete.as_view())),
    url(r'^add_moderator/(?P<pk>\d+)/$', login_required(SkillModerCreate.as_view())),
    url(r'^delete_moderator/(?P<pk>\d+)/$', login_required(SkillModerDelete.as_view())),
    url(r'^add_editor/(?P<pk>\d+)/$', login_required(SkillEditorCreate.as_view())),
    url(r'^delete_editor/(?P<pk>\d+)/$', login_required(SkillEditorDelete.as_view())),
    url(r'^add_advertiser/(?P<pk>\d+)/$', login_required(SkillAdvertiserCreate.as_view())),
    url(r'^delete_advertiser/(?P<pk>\d+)/$', login_required(SkillAdvertiserDelete.as_view())),
    url(r'^add_teacher/(?P<pk>\d+)/$', login_required(SkillTeacherCreate.as_view())),
    url(r'^delete_teacher/(?P<pk>\d+)/$', login_required(SkillTeacherDelete.as_view())),

    url(r'^add_worker_admin/(?P<pk>\d+)/$', login_required(SkillWorkerAdminCreate.as_view())),
    url(r'^delete_worker_admin/(?P<pk>\d+)/$', login_required(SkillWorkerAdminDelete.as_view())),
    url(r'^add_worker_moderator/(?P<pk>\d+)/$', login_required(SkillWorkerModerCreate.as_view())),
    url(r'^delete_worker_moderator/(?P<pk>\d+)/$', login_required(SkillWorkerModerDelete.as_view())),
    url(r'^add_worker_editor/(?P<pk>\d+)/$', login_required(SkillWorkerEditorCreate.as_view())),
    url(r'^delete_worker_editor/(?P<pk>\d+)/$', login_required(SkillWorkerEditorDelete.as_view())),
    url(r'^add_worker_advertiser/(?P<pk>\d+)/$', login_required(SkillWorkerAdvertiserCreate.as_view())),
    url(r'^delete_worker_advertiser/(?P<pk>\d+)/$', login_required(SkillWorkerAdvertiserDelete.as_view())),
    url(r'^add_worker_teacher/(?P<pk>\d+)/$', login_required(SkillWorkerTeacherCreate.as_view())),
    url(r'^delete_worker_teacher/(?P<pk>\d+)/$', login_required(SkillWorkerTeacherDelete.as_view())),
]
