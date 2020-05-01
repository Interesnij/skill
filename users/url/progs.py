from django.conf.urls import url
from users.view.progs import (
                                UserBanCreate,
                                UserUnbanCreate,
                                UserAdView,
                                PhoneSend,
                                PhoneVerify,
                                AddSubscribe,
                                DeleteSubscribe
                            )
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^block/(?P<pk>\d+)/$', login_required(UserBanCreate.as_view())),
    url(r'^unblock/(?P<pk>\d+)/$', login_required(UserUnbanCreate.as_view())),
    url(r'^ad_view/(?P<pk>\d+)/$', login_required(UserAdView.as_view())),
    url(r'^phone_send/(?P<phone>\d+)/$', login_required(PhoneSend.as_view())),
    url(r'^phone_verify/(?P<phone>\d+)/(?P<code>\d+)/$', login_required(PhoneVerify.as_view())),

    url(r'^subscribe/(?P<pk>\d+)/$', login_required(AddSubscribe.as_view())),
    url(r'^unsubscribe/(?P<pk>\d+)/$', login_required(DeleteSubscribe.as_view())),
]
