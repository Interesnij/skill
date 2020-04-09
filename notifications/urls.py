from django.conf.urls import url

from notifications.views import *


urlpatterns = [
    url(r'^user/$', NotificationListView.as_view()),
    #url(r'^user_all_read/$', user_all_read, name='user_all_read'),
    #url(r'^latest-notifications/$', get_latest_notifications),
]
