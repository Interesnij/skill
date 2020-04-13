from django.conf.urls import url, include
from main.views import MainPageView, MainPhoneSend


urlpatterns = [
	url(r'^$', MainPageView.as_view(), name="main"),
	url(r'^phone_send/$', MainPhoneSend.as_view(), name="phone_sendd"),
]
