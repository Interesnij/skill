from django.views.generic.base import TemplateView
from django.views.generic import ListView
from users.models import User
from django.db.models import Q


class GetAdManage(ListView):
    template_name = None
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_ad_staff_worker() or request.user.is_superuser:
            self.template_name = self.user.get_my_template(folder="manage/", template="ad_staff.html", request=request)
        else:
            self.template_name = "generic/permisson_error.html"
        return super(GetAdManage,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        from logs.models import AdWorkerLog
        context = super(GetAdManage, self).get_context_data(**kwargs)
        context['user'] = self.user
        context['logs'] = AdWorkerLog.objects.only("pk")
        return context

    def get_queryset(self):
        managers = self.user.get_ads_managers()
        return managers


class GetSkillManage(ListView):
    template_name = None
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_skill_staff_worker() or request.user.is_superuser:
            self.template_name = self.user.get_my_template(folder="manage/", template="skill_staff.html", request=request)
        else:
            self.template_name = "generic/permisson_error.html"
        return super(GetSkillManage,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        from logs.models import SkillWorkerLog
        context = super(GetSkillManage, self).get_context_data(**kwargs)
        context['user'] = self.user
        context['logs'] = SkillWorkerLog.objects.only("pk")
        return context

    def get_queryset(self):
        managers = self.user.get_skills_managers()
        return managers


class GetAnketsManage(ListView):
    template_name = None
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_anketa_staff_worker() or request.user.is_superuser:
            self.template_name = self.user.get_my_template(folder="manage/", template="ankets_staff.html", request=request)
        else:
            self.template_name = "generic/permisson_error.html"
        return super(GetAnketsManage,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        from logs.models import AnketaWorkerLog
        context = super(GetAnketsManage, self).get_context_data(**kwargs)
        context['user'] = self.user
        context['logs'] = AnketaWorkerLog.objects.only("pk")
        return context

    def get_queryset(self):
        managers = self.user.get_ankets_managers()
        return managers


class GetStaffManage(ListView):
    template_name = None
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_staff_worker() or request.user.is_superuser:
            self.template_name = self.user.get_my_template(folder="manage/", template="users_staff.html", request=request)
        else:
            self.template_name = "generic/permisson_error.html"
        return super(GetStaffManage,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        from logs.models import UserWorkerLog
        context = super(GetStaffManage, self).get_context_data(**kwargs)
        context['user'] = self.user
        context['logs'] = UserWorkerLog.objects.only("pk")
        return context

    def get_queryset(self):
        managers = self.user.get_managers()
        return managers
