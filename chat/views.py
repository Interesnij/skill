from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class MessagesListView(LoginRequiredMixin,TemplateView):
    template_name = "message_list.html"
