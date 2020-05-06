from django.views.generic.base import TemplateView
from skill_posts.models import Course
from regions.models import Region
from skill_categories.models import SkillCategory, SkillSubCategory
from django.http import HttpResponse


class SkillPostsView(TemplateView):
    template_name = "skill_posts.html"


class CourseDetailView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        from common.get_templates import get_template_course_detail

        self.course = Course.objects.get(pk=self.kwargs["pk"])
        self.template_name = get_template_course_detail(course=self.course, folder="detail/", template="course.html", request=request)
        return super(CourseDetailView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['course'] = self.course
        return context


class CourseCreate(TemplateView):
    template_name="course_add.html"

    def get_context_data(self,**kwargs):
        context=super(AdCreate,self).get_context_data(**kwargs)
        context['skill_categories'] = SkillCategory.objects.only("pk")
        return context
