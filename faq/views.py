from django.views.generic import ListView
from faq.models import Quan


class FaqView(ListView):
    template_name = None
    model = Quan
    paginate_by = 30

    def get(self,request,*args,**kwargs):
		import re

		if not request.user.is_deleted:
			self.template_name = "faq/faq.html"
		else:
			self.template_name = "generic/user_deleted.html"

		MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
		if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
			self.template_name = "mob_" + self.template_name
		return super(FaqView,self).get(request,*args,**kwargs)

    def get_queryset(self):
        quans = Quan.models.only("pk")
        return quans
