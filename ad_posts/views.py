from django.views.generic.base import TemplateView
from ad_posts.models import Ad


class AdPostsView(TemplateView):
    template_name = "ad_posts.html"


class AdDetailView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.ad = Ad.objects.get(pk=self.kwargs["pk"])
        self.template_name = request.user.get_template_ad_detail(ad=self.ad, folder="detail/", template="_cat.html", request=request)
        return super(AdDetailView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdDetailView, self).get_context_data(**kwargs)
        context['ad'] = self.ad
        return context


class AdCreate(TemplateView):
	template_name="ad_add.html"
	success_url="/"

	def get(self,request,*args,**kwargs):
		return super(AdCreate,self).get(request,*args,**kwargs)
	def get_context_data(self,**kwargs):
		context=super(AdCreate,self).get_context_data(**kwargs)
		return context
