from django.views.generic.base import TemplateView
from cities.models import City


class CityView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.city = City.objects.get(name_en=self.kwargs["city_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "city/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "city/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(CityView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(CityView, self).get_context_data(**kwargs)
        context['city'] = self.city
        return context
