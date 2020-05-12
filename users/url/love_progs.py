from django.conf.urls import url
from users.view.love_progs import (
                                    AnketaActive,
                                    AnketaUnActive,
                                    AnketaDelete,
                                    AnketaUnDelete,
                                    AnketaFavorite,
                                    AnketaUnFavorite,

                                    AnketaAdminCreate,
                                    AnketaAdminDelete,
                                    AnketaModerCreate,
                                    AnketaModerDelete,
                                    AnketaEditorCreate,
                                    AnketaEditorDelete,
                                    AnketaAdvertiserCreate,
                                    AnketaAdvertiserDelete,

                                    AnketaWorkerAdminCreate,
                                    AnketaWorkerAdminDelete,
                                    AnketaWorkerModerCreate,
                                    AnketaWorkerModerDelete,
                                    AnketaWorkerEditorCreate,
                                    AnketaWorkerEditorDelete,
                                    AnketaWorkerAdvertiserCreate,
                                    AnketaWorkerAdvertiserDelete
                                )
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^active/(?P<pk>\d+)/$', login_required(AnketaActive.as_view())),
    url(r'^unactive/(?P<pk>\d+)/$', login_required(AnketaUnActive.as_view())),
    url(r'^delete/(?P<pk>\d+)/$', login_required(AnketaDelete.as_view())),
    url(r'^undelete/(?P<pk>\d+)/$', login_required(AnketaUnDelete.as_view())),

    url(r'^favorite/(?P<pk>\d+)/$', login_required(AnketaFavorite.as_view())),
    url(r'^unfavorite/(?P<pk>\d+)/$', login_required(AnketaUnFavorite.as_view())),

    url(r'^add_admin/(?P<pk>\d+)/$', login_required(AnketaAdminCreate.as_view())),
    url(r'^delete_admin/(?P<pk>\d+)/$', login_required(AnketaAdminDelete.as_view())),
    url(r'^add_moderator/(?P<pk>\d+)/$', login_required(AnketaModerCreate.as_view())),
    url(r'^delete_moderator/(?P<pk>\d+)/$', login_required(AnketaModerDelete.as_view())),
    url(r'^add_editor/(?P<pk>\d+)/$', login_required(AnketaEditorCreate.as_view())),
    url(r'^delete_editor/(?P<pk>\d+)/$', login_required(AnketaEditorDelete.as_view())),
    url(r'^add_advertiser/(?P<pk>\d+)/$', login_required(AnketaAdvertiserCreate.as_view())),
    url(r'^delete_advertiser/(?P<pk>\d+)/$', login_required(AnketaAdvertiserDelete.as_view())),

    url(r'^add_worker_admin/(?P<pk>\d+)/$', login_required(AnketaWorkerAdminCreate.as_view())),
    url(r'^delete_worker_admin/(?P<pk>\d+)/$', login_required(AnketaWorkerAdminDelete.as_view())),
    url(r'^add_worker_moderator/(?P<pk>\d+)/$', login_required(AnketaWorkerModerCreate.as_view())),
    url(r'^delete_worker_moderator/(?P<pk>\d+)/$', login_required(AnketaWorkerModerDelete.as_view())),
    url(r'^add_worker_editor/(?P<pk>\d+)/$', login_required(AnketaWorkerEditorCreate.as_view())),
    url(r'^delete_worker_editor/(?P<pk>\d+)/$', login_required(AnketaWorkerEditorDelete.as_view())),
    url(r'^add_worker_advertiser/(?P<pk>\d+)/$', login_required(AnketaWorkerAdvertiserCreate.as_view())),
    url(r'^delete_worker_advertiser/(?P<pk>\d+)/$', login_required(AnketaWorkerAdvertiserDelete.as_view())),
]
