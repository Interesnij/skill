from django.views.generic.base import TemplateView
from common.utils import get_client_ip, get_location
from users.models import User


class StatView(TemplateView):
    template_name = "stat.html"

    def get(self,request,*args,**kwargs):
        self.ip = get_client_ip(request)
        get_location(request)
        return super(StatView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(StatView,self).get_context_data(**kwargs)
        context["ip"] = self.ip
        return context

class StatAdView(TemplateView):
    template_name = "item_stat.html"

    def get(self,request,*args,**kwargs):
        from ad_posts.models import Ad

        self.ad = Ad.objects.get(uuid=self.kwargs["uuid"])
        return super(StatAdView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(StatAdView,self).get_context_data(**kwargs)
        context["ad"] = self.ad
        return context
