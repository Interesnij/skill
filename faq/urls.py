from django.conf.urls import url
from faq.views import FaqView


urlpatterns = [
    url(r'^$', FaqView.as_view(), name='faq'),
]
