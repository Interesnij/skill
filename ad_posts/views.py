from django.views.generic.base import TemplateView
from ad_posts.models import Ad


class AdPostsView(TemplateView):
    template_name = "ad_posts.html"


class AdDetailView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.user = request.user
        self.ad = Ad.objects.get(pk=self.kwargs["pk"])
        self.cat_pk = self.ad.category.category.pk
        self.template_name = self.user.get_template_ad_detail(folder="detail/", template=str(self.cat_pk) + "_page.html", request=request)
        return super(AdDetailView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdDetailView, self).get_context_data(**kwargs)
        context['ad'] = self.ad
        return context
