from django.views import View
from users.models import User
from django.http import HttpResponse
from skill_posts.models import Course, CourseFavourites


class SkillActive(View):
    def get(self,request,*args,**kwargs):
        course = Course.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == course.creator.pk and course.is_active != True:
            course.is_active = True
            course.save(update_fields=['is_active'])
            return HttpResponse('')
        else:
            return HttpResponse('')


class SkillUnActive(View):
    def get(self,request,*args,**kwargs):
        course = Course.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == course.creator.pk and course.is_active != False:
            course.is_active = False
            course.save(update_fields=['is_active'])
            return HttpResponse('')
        else:
            return HttpResponse('')


class SkillDelete(View):
    def get(self,request,*args,**kwargs):
        course = Course.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == course.creator.pk and course.is_deleted != True:
            course.is_deleted = True
            course.is_active = False
            course.save(update_fields=['is_deleted', 'is_active'])
            return HttpResponse('')
        else:
            return HttpResponse('')


class SkillUnDelete(View):
    def get(self,request,*args,**kwargs):
        course = Course.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == course.creator.pk and course.is_deleted != False:
            course.is_deleted = False
            course.save(update_fields=['is_deleted'])
            return HttpResponse('')
        else:
            return HttpResponse('')


class SkillFavorite(View):
    def get(self,request,*args,**kwargs):
        course = Course.objects.get(pk=self.kwargs["pk"])
        if request.user.pk != course.creator.pk and course.is_deleted != True:
            CourseFavourites.objects.create(course=course, user=request.user)
            return HttpResponse('')
        else:
            return HttpResponse('')


class SkillUnFavorite(View):
    def get(self,request,*args,**kwargs):
        course = Course.objects.get(pk=self.kwargs["pk"])
        try:
            favorite = CourseFavourites.objects.get(course=course, user=request.user)
            favorite.delete()
            return HttpResponse('')
        except:
            return HttpResponse('')
