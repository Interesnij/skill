from django.views.generic.base import TemplateView
from ad_posts.models import Ad
from ad_categories.models import AdCategory, AdSubCategory
from django.http import HttpResponse


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
        context['ad_categories'] = AdCategory.objects.only("pk")
        return context


class FormAdd(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.subcat = AdSubCategory.objects.get(pk=self.kwargs["pk"])
        form_1 = "Form_1"

        from ad_posts.forms import {}.format(form_1) as Form

        self.template_name = "forms/" + str(self.subcat.order) + ".html"
        self.form = Form(initial={"creator":request.user})
        return super(FormAdd,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(FormAdd,self).get_context_data(**kwargs)
        context["form"]=self.form
        return context

    def post(self,request,*args,**kwargs):
        self.form = Form(request.POST,request.FILES)
        if self.form.is_valid():
            ad = self.form.save(commit=False)
            ad.creator = self.request.user
            ad = self.form.save()
            return HttpResponse ('')
        return super(FormAdd,self).get(request,*args,**kwargs)
