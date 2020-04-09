from django.views.generic.base import TemplateView


class ProfileUserView(TemplateView):
    template_name = "user.html"
