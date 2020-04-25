from django.views.generic.base import TemplateView
from django.views.generic import ListView
from skill_categories.models import SkillCategory, SkillSubCategory
from skill_posts.models import Course
from regions.models import Region
from cities.models import City


class SkillCategoriesView(TemplateView):
    template_name = "skill_categories.html"


class SkillCategoryView(ListView):
    template_name = None
    model = Course
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.cat=SkillCategory.objects.get(name_en=self.kwargs["cat_name"])
        if request.user.is_authenticated and not request.user.is_deleted:
            self.template_name = "skill_cat/page.html"
        elif request.user.is_authenticated and request.user.is_deleted:
            self.template_name = "generic/user_deleted.html"
        elif request.user.is_anonymous:
            self.template_name = "skill_cat/anon_page.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(SkillCategoryView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(SkillCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        context['skill_categories'] = SkillCategory.objects.only("pk")
        return context

    def get_queryset(self):
        ads = self.cat.get_ads()
        return ads
