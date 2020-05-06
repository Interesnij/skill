from django.views.generic.base import TemplateView
from love_posts.models import Anketa
from regions.models import Region
from django.http import HttpResponse


class LovePostsView(TemplateView):
    template_name = "love_posts.html"


class AnketaDetailView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        from common.get_templates import get_template_anketa_detail

        self.anketa = Anketa.objects.get(pk=self.kwargs["pk"])
        self.template_name = get_template_anketa_detail(anketa=self.anketa, folder="detail/", template="anketa.html", request=request)
        return super(AnketaDetailView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AnketaDetailView, self).get_context_data(**kwargs)
        context['anketa'] = self.anketa
        return context


class AnketaCreate(TemplateView):
    template_name="anketa_add.html"

    def get_context_data(self,**kwargs):
        context=super(AnketaCreate,self).get_context_data(**kwargs)
        return context
