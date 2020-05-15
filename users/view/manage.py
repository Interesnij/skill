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
        context = super(GetAdManage, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context

    def get_queryset(self):
        from users.model.profile import CanAddStaffAdUser
        managers = CanAddStaffAdUser.objects.all().values('user_id')
        managers_ids = [user['user_id'] for user in managers]
        users = Q(id__in=managers_ids)
        managers_query = User.objects.filter(users)
        return managers_query


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
        context = super(GetSkillManage, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context

    def get_queryset(self):
        users = User.objects.only("can_work_staff_skill_user__id")
        return users


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
        context = super(GetAnketsManage, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context

    def get_queryset(self):
        users = User.objects.only("can_work_staff_anketa_user__id")
        return users


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
        context = super(GetStaffManage, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context

    def get_queryset(self):
        users = User.objects.only("can_work_staff_user__id")
        return users
