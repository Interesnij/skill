from django.views.generic.base import TemplateView
from django.views.generic import ListView
from users.models import User
from ad_posts.models import Ad
from skill_posts.models import Course


class ProfileUserView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_template_user(folder="user/", template="user.html", request=request)
        return super(ProfileUserView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileUserView, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context


class UserAdsView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_my_template(folder="list/", template="ads.html", request=request)
        return super(UserAdsView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserAdsView, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context

    def get_queryset(self):
        ads = self.user.get_my_ads()
        return ads


class UserCoursesView(ListView):
    template_name = None
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_my_template(folder="list/", template="courses.html", request=request)
        return super(UserCoursesView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserCoursesView, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context

    def get_queryset(self):
        courses = self.user.get_my_courses()
        return courses


class UserAnketsView(ListView):
    template_name = None
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_my_template(folder="list/", template="ankets.html", request=request)
        return super(UserAnketsView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserAnketsView, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context

    def get_queryset(self):
        courses = self.user.get_my_ankets()
        return courses


class UserFavoriteView(ListView):
    template_name = None
    model = Ad
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_my_template(folder="list/", template="favorites.html", request=request)
        return super(UserFavoriteView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserFavoriteView, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context

    def get_queryset(self):
        ads = self.user.get_my_favorite_ads()
        return ads


class MySubscribeView(ListView):
    template_name = None
    model = User
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_my_template(folder="list/", template="my_subscribe.html", request=request)
        return super(MySubscribeView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(MySubscribeView, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context

    def get_queryset(self):
        users = self.user.get_my_subscribs()
        return users


class SubscribesView(ListView):
    template_name = None
    model = User
    paginate_by = 30

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_my_template(folder="list/", template="subscribes.html", request=request)
        return super(SubscribesView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(SubscribesView, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context

    def get_queryset(self):
        users = self.user.get_subscribs()
        return users


class UserSettingsView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_my_template(folder="list/", template="settings.html", request=request)
        return super(UserSettingsView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserSettingsView, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context
