from django.views import View
from users.models import User
from django.http import HttpResponse
from ad_posts.models import Ad, AdFavourites
from logs.models import AdWorkerLog, AdManageCreatorLog


class AdSold(View):
    def get(self,request,*args,**kwargs):
        ad = Ad.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == ad.creator.pk and ad.is_sold != True:
            ad.is_sold = True
            ad.is_active = False
            ad.save(update_fields=['is_sold', 'is_active'])
            return HttpResponse('')
        else:
            return HttpResponse('')

class AdUnSold(View):
    def get(self,request,*args,**kwargs):
        ad = Ad.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == ad.creator.pk and ad.is_sold != False:
            ad.is_sold = False
            ad.is_active = True
            ad.save(update_fields=['is_sold', 'is_active'])
            return HttpResponse('')
        else:
            return HttpResponse('')


class AdActive(View):
    def get(self,request,*args,**kwargs):
        ad = Ad.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == ad.creator.pk and ad.is_active != True:
            ad.is_active = True
            ad.save(update_fields=['is_active'])
            return HttpResponse('')
        else:
            return HttpResponse('')


class AdUnActive(View):
    def get(self,request,*args,**kwargs):
        ad = Ad.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == ad.creator.pk and ad.is_active != False:
            ad.is_active = False
            ad.save(update_fields=['is_active'])
            return HttpResponse('')
        else:
            return HttpResponse('')


class AdDelete(View):
    def get(self,request,*args,**kwargs):
        ad = Ad.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == ad.creator.pk and ad.is_deleted != True:
            ad.is_deleted = True
            ad.is_active = False
            ad.save(update_fields=['is_deleted', 'is_active'])
            return HttpResponse('')
        else:
            return HttpResponse('')


class AdUnDelete(View):
    def get(self,request,*args,**kwargs):
        ad = Ad.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == ad.creator.pk and ad.is_deleted != False:
            ad.is_deleted = False
            ad.save(update_fields=['is_deleted'])
            return HttpResponse('')
        else:
            return HttpResponse('')


class AdFavorite(View):
    def get(self,request,*args,**kwargs):
        ad = Ad.objects.get(pk=self.kwargs["pk"])
        if request.user.pk != ad.creator.pk and ad.is_deleted != True:
            AdFavourites.objects.create(ad=ad, user=request.user)
            return HttpResponse('')
        else:
            return HttpResponse('')


class AdUnFavorite(View):
    def get(self,request,*args,**kwargs):
        ad = Ad.objects.get(pk=self.kwargs["pk"])
        try:
            favorite = AdFavourites.objects.get(ad=ad, user=request.user)
            favorite.delete()
            return HttpResponse('')
        except:
            return HttpResponse('')


class AdAdminCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_administrator:
            user.add_ad_administrator()
            AdWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен админ объявлений')
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdAdminDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_administrator:
            user.remove_ad_administrator()
            AdWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален админ объявлений')
        return HttpResponse("")


class AdModerCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_moderator:
            user.add_ad_moderator()
            AdWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен модератор объявлений')
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdModerDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_moderator:
            user.remove_ad_moderator()
            AdWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален модератор объявлений')
        return HttpResponse("")


class AdEditorCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_editor:
            user.add_ad_editor()
            AdWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен редактор объявлений')
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdEditorDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_editor:
            user.remove_ad_editor()
            AdWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален редактор объявлений')
        return HttpResponse("")


class AdAdvertiserCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_advertiser:
            user.add_ad_advertiser()
            AdWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен рекламодатель объявлений')
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdAdvertiserDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_advertiser:
            user.remove_ad_advertiser()
            AdWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален рекламодатель объявлений')
        return HttpResponse("")



class AdWorkerAdminCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_ad_administrator_worker()
            AdManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель админов объявлений')
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdWorkerAdminDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_ad_administrator_worker()
            AdManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель админов объявлений')
        return HttpResponse("")


class AdWorkerModerCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_ad_moderator_worker()
            return HttpResponse("")
            AdManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель модераторов объявлений')
        else:
            return HttpResponse("")

class AdWorkerModerDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_ad_moderator_worker()
            AdManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель модераторов объявлений')
        return HttpResponse("")


class AdWorkerEditorCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_ad_editor_worker()
            AdManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель редакторов объявлений')
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdWorkerEditorDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_ad_editor_worker()
            AdManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель редакторов объявлений')
        return HttpResponse("")


class AdWorkerAdvertiserCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_ad_advertiser_worker()
            AdManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель рекламодателей объявлений')
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdWorkerAdvertiserDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_ad_advertiser_worker()
            AdManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель рекламодателей объявлений')
        return HttpResponse("")
