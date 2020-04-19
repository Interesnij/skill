from django.views.generic.base import TemplateView
from ad_posts.models import Ad
from regions.models import Region
from ad_categories.models import AdCategory, AdSubCategory
from django.http import HttpResponse
from common.utils import get_current_form
from ad_posts.forms import Form_1


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

    def get_context_data(self,**kwargs):
        context=super(AdCreate,self).get_context_data(**kwargs)
        context['ad_categories'] = AdCategory.objects.only("pk")
        context['regions'] = Region.objects.only("pk")
        return context


class FormAdd(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.subcat = AdSubCategory.objects.get(pk=self.kwargs["pk"])
        if self.kwargs["pk"] in [1,2]:
            from ad_posts.forms import Form_1
            self.form = Form_1
        self.template_name = "forms/cat_" + str(self.subcat.category.order) + "/sub_" + str(self.subcat.order) + ".html"
        return super(FormAdd,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(FormAdd,self).get_context_data(**kwargs)
        context["form"] = self.form
        return context

    def post(self,request,*args,**kwargs):
        self.form = get_current_form(self.kwargs["pk"])
        if self.form.is_valid():
            ad = self.form.save(commit=False)
            ad.creator = self.request.user
            ad = self.form.save()
            return HttpResponse ('')
        return super(FormAdd,self).get(request,*args,**kwargs)
