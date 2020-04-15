from django.views.generic.base import TemplateView
from django.views.generic import ListView
from regions.models import Region
import re
from ad_posts.models import Ad


class RegionView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.region = Region.objects.get(name_en=self.kwargs["region_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "region/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "region/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(RegionView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(RegionView, self).get_context_data(**kwargs)
        context['region'] = self.region
        return context

    def get_queryset(self):
        ads = self.region.get_ads()
        return ads
