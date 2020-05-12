from django.views import View
from users.models import User
from django.http import HttpResponse
from love_posts.models import Anketa, AnketaFavourites


class AnketaActive(View):
    def get(self,request,*args,**kwargs):
        anketa = Anketa.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == anketa.creator.pk and anketa.is_active != True:
            anketa.is_active = True
            anketa.save(update_fields=['is_active'])
            return HttpResponse('')
        else:
            return HttpResponse('')

class AnketaUnActive(View):
    def get(self,request,*args,**kwargs):
        anketa = Anketa.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == anketa.creator.pk and anketa.is_active != False:
            anketa.is_active = False
            anketa.save(update_fields=['is_active'])
            return HttpResponse('')
        else:
            return HttpResponse('')


class AnketaDelete(View):
    def get(self,request,*args,**kwargs):
        anketa = Anketa.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == anketa.creator.pk and anketa.is_deleted != True:
            anketa.is_deleted = True
            anketa.is_active = False
            anketa.save(update_fields=['is_deleted', 'is_active'])
            return HttpResponse('')
        else:
            return HttpResponse('')

class AnketaUnDelete(View):
    def get(self,request,*args,**kwargs):
        anketa = Anketa.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == anketa.creator.pk and anketa.is_deleted != False:
            anketa.is_deleted = False
            anketa.save(update_fields=['is_deleted'])
            return HttpResponse('')
        else:
            return HttpResponse('')


class AnketaFavorite(View):
    def get(self,request,*args,**kwargs):
        anketa = Anketa.objects.get(pk=self.kwargs["pk"])
        if request.user.pk != anketa.creator.pk and anketa.is_deleted != True:
            AnketaFavourites.objects.create(anketa=anketa, user=request.user)
            return HttpResponse('')
        else:
            return HttpResponse('')

class AnketaUnFavorite(View):
    def get(self,request,*args,**kwargs):
        anketa = Anketa.objects.get(pk=self.kwargs["pk"])
        try:
            favorite = AnketaFavourites.objects.get(anketa=anketa, user=request.user)
            favorite.delete()
            return HttpResponse('')
        except:
            return HttpResponse('')


class AnketaAdminCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_anketa_administrator:
            user.add_anketa_administrator()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AnketaAdminDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_anketa_administrator:
            user.remove_anketa_administrator()
        return HttpResponse("")


class AnketaModerCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_anketa_moderator:
            user.add_anketa_moderator()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AnketaModerDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_anketa_moderator:
            user.remove_anketa_moderator()
        return HttpResponse("")


class AnketaEditorCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_anketa_editor:
            user.add_anketa_editor()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AnketaEditorDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_anketa_editor:
            user.remove_anketa_editor()
        return HttpResponse("")


class AnketaAdvertiserCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_anketa_advertiser:
            user.add_anketa_advertiser()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AnketaAdvertiserDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_anketa_advertiser:
            user.remove_anketa_advertiser()
        return HttpResponse("")


class AnketaWorkerAdminCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_anketa_administrator_worker()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AnketaWorkerAdminDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_anketa_administrator_worker()
        return HttpResponse("")


class AnketaWorkerModerCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_anketa_moderator_worker()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AnketaWorkerModerDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_anketa_moderator_worker()
        return HttpResponse("")


class AnketaWorkerEditorCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_anketa_editor_worker()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AnketaWorkerEditorDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_anketa_editor_worker()
        return HttpResponse("")


class AnketaWorkerAdvertiserCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_anketa_advertiser:
            user.add_anketa_advertiser()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AnketaWorkerAdvertiserDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_anketa_advertiser:
            user.remove_anketa_advertiser()
        return HttpResponse("")
