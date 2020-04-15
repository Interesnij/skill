from django.views.generic.base import TemplateView
from django.views.generic import ListView
import re
from ad_categories.models import AdCategory, AdSubCategory
from ad_posts.models import Ad


class AdCategoriesView(TemplateView):
    template_name = "ad_categories.html"


class AdCategoryView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.cat=AdCategory.objects.get(name_en=self.kwargs["cat_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "ad_cat/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "ad_cat/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(AdCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        return context

    def get_queryset(self):
        ads = self.cat.get_ads()
        return ads


class AdSubCategoryView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.cat=AdSubCategory.objects.get(name_en=self.kwargs["subcat_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "ad_subcat/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "ad_subcat/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(AdSubCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdSubCategoryView, self).get_context_data(**kwargs)
        context['sub_category'] = self.cat
        return context

    def get_queryset(self):
        ads = self.cat.get_ads()
        return ads
