from django.views.generic import ListView
from faq.models import Quan


class FaqView(ListView):
    template_name = None
    model = Quan
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        import re

        if not request.user.is_deleted and not request.user.is_blocked:
            self.template_name = "faq/faq.html"
        elif request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_blocked:
            self.template_name = "generic/you_are_block.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(FaqView,self).get(request,*args,**kwargs)

    def get_queryset(self):
        quans = Quan.objects.only("pk")
        return quans
