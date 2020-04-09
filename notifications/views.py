rom django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class ItemNotificationListView(LoginRequiredMixin, TEmplateView):
    template_name = 'user_notify_list.html'
