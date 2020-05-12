from django.conf.urls import url
from users.view.ad_progs import (
                                    AdSold,
                                    AdUnSold,
                                    AdActive,
                                    AdUnActive,
                                    AdDelete,
                                    AdUnDelete,
                                    AdFavorite,
                                    AdUnFavorite,

                                    AdAdminCreate,
                                    AdAdminDelete,
                                    AdModerCreate,
                                    AdModerDelete,
                                    AdEditorCreate,
                                    AdEditorDelete,
                                    AdAdvertiserCreate,
                                    AdAdvertiserDelete,

                                    AdWorkerAdminCreate,
                                    AdWorkerAdminDelete,
                                    AdWorkerModerCreate,
                                    AdWorkerModerDelete,
                                    AdWorkerEditorCreate,
                                    AdWorkerEditorDelete,
                                    AdWorkerAdvertiserCreate,
                                    AdWorkerAdvertiserDelete
                                )
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^sold/(?P<pk>\d+)/$', login_required(AdSold.as_view())),
    url(r'^unsold/(?P<pk>\d+)/$', login_required(AdUnSold.as_view())),
    url(r'^active/(?P<pk>\d+)/$', login_required(AdActive.as_view())),
    url(r'^unactive/(?P<pk>\d+)/$', login_required(AdUnActive.as_view())),
    url(r'^delete/(?P<pk>\d+)/$', login_required(AdDelete.as_view())),
    url(r'^undelete/(?P<pk>\d+)/$', login_required(AdUnDelete.as_view())),

    url(r'^favorite/(?P<pk>\d+)/$', login_required(AdFavorite.as_view())),
    url(r'^unfavorite/(?P<pk>\d+)/$', login_required(AdUnFavorite.as_view())),

    url(r'^add_admin/(?P<pk>\d+)/$', login_required(AdAdminCreate.as_view())),
    url(r'^delete_admin/(?P<pk>\d+)/$', login_required(AdAdminDelete.as_view())),
    url(r'^add_moderator/(?P<pk>\d+)/$', login_required(AdModerCreate.as_view())),
    url(r'^delete_moderator/(?P<pk>\d+)/$', login_required(AdModerDelete.as_view())),
    url(r'^add_editor/(?P<pk>\d+)/$', login_required(AdEditorCreate.as_view())),
    url(r'^delete_editor/(?P<pk>\d+)/$', login_required(AdEditorDelete.as_view())),
    url(r'^add_advertiser/(?P<pk>\d+)/$', login_required(AdAdvertiserCreate.as_view())),
    url(r'^delete_advertiser/(?P<pk>\d+)/$', login_required(AdAdvertiserDelete.as_view())),

    url(r'^add_worker_admin/(?P<pk>\d+)/$', login_required(AdWorkerAdminCreate.as_view())),
    url(r'^delete_worker_admin/(?P<pk>\d+)/$', login_required(AdWorkerAdminDelete.as_view())),
    url(r'^add_worker_moderator/(?P<pk>\d+)/$', login_required(AdWorkerModerCreate.as_view())),
    url(r'^delete_worker_moderator/(?P<pk>\d+)/$', login_required(AdWorkerModerDelete.as_view())),
    url(r'^add_worker_editor/(?P<pk>\d+)/$', login_required(AdWorkerEditorCreate.as_view())),
    url(r'^delete_worker_editor/(?P<pk>\d+)/$', login_required(AdWorkerEditorDelete.as_view())),
    url(r'^add_worker_advertiser/(?P<pk>\d+)/$', login_required(AdWorkerAdvertiserCreate.as_view())),
    url(r'^delete_worker_advertiser/(?P<pk>\d+)/$', login_required(AdWorkerAdvertiserDelete.as_view())),
]
