from django.views import View
from users.models import User
from django.http import HttpResponse
from skill_posts.models import Course, CourseFavourites
from logs.models import SkillWorkerLog, SkillManageCreatorLog


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


class SkillAdminCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_anketa_administrator:
            user.add_skill_administrator()
            SkillWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен админ академии')
            return HttpResponse("")
        else:
            return HttpResponse("")

class SkillAdminDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_skill_administrator:
            user.remove_skill_administrator()
            SkillWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален админ академии')
        return HttpResponse("")


class SkillModerCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_skill_moderator:
            user.add_skill_moderator()
            SkillWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен модератор академии')
            return HttpResponse("")
        else:
            return HttpResponse("")

class SkillModerDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_skill_moderator:
            user.remove_skill_moderator()
            SkillWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален модератор академии')
        return HttpResponse("")


class SkillEditorCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_skill_editor:
            user.add_skill_editor()
            SkillWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен редактор академии')
            return HttpResponse("")
        else:
            return HttpResponse("")

class SkillEditorDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_skill_editor:
            user.remove_skill_editor()
            SkillWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален редактор академии')
        return HttpResponse("")


class SkillAdvertiserCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_skill_advertiser:
            user.add_skill_advertiser()
            SkillWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен рекламодатель академии')
            return HttpResponse("")
        else:
            return HttpResponse("")

class SkillAdvertiserDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_skill_advertiser:
            user.remove_skill_advertiser()
            SkillWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален рекламодатель академии')
        return HttpResponse("")


class SkillTeacherCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_skill_advertiser:
            user.add_skill_teacher()
            SkillWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен учитель академии')
            return HttpResponse("")
        else:
            return HttpResponse("")

class SkillTeacherDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_skill_advertiser:
            user.remove_skill_teacher()
            SkillWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален учитель академии')
        return HttpResponse("")


class SkillWorkerAdminCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_anketa_administrator_worker()
            SkillManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель админов академии')
            return HttpResponse("")
        else:
            return HttpResponse("")

class SkillWorkerAdminDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_skill_administrator_worker()
            SkillManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель админов академии')
        return HttpResponse("")


class SkillWorkerModerCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_skill_moderator_worker()
            SkillManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель модераторов академии')
            return HttpResponse("")
        else:
            return HttpResponse("")

class SkillWorkerModerDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_skill_moderator_worker()
            SkillManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель модераторов академии')
        return HttpResponse("")


class SkillWorkerEditorCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_skill_editor_worker()
            SkillManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель редакторов академии')
            return HttpResponse("")
        else:
            return HttpResponse("")

class SkillWorkerEditorDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_skill_editor_worker()
            SkillManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель редакторов академии')
        return HttpResponse("")


class SkillWorkerAdvertiserCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_skill_advertiser_worker()
            SkillManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель рекламодателей академии')
            return HttpResponse("")
        else:
            return HttpResponse("")

class SkillWorkerAdvertiserDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_skill_advertiser_worker()
            SkillManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель рекламодателей академии')
        return HttpResponse("")


class SkillWorkerTeacherCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_skill_teacher_worker()
            SkillManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель учителей академии')
            return HttpResponse("")
        else:
            return HttpResponse("")

class SkillWorkerTeacherDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_skill_teacher_worker()
            SkillManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель учителей академии')
        return HttpResponse("")
