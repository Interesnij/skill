from django.conf.urls import url
from chat.views import *


urlpatterns = [
    url(r'^$', MessagesListView.as_view(), name='messages_list'),
]
