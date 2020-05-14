from django.views import View
from users.models import User
from django.http import HttpResponse
from ad_posts.models import Ad, AdFavourites


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
            user.add_ad_administrator(request.user)
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdAdminDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_administrator:
            user.remove_ad_administrator()
        return HttpResponse("")


class AdModerCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_moderator:
            user.add_ad_moderator()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdModerDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_moderator:
            user.remove_ad_moderator()
        return HttpResponse("")


class AdEditorCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_editor:
            user.add_ad_editor()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdEditorDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_editor:
            user.remove_ad_editor()
        return HttpResponse("")


class AdAdvertiserCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_advertiser:
            user.add_ad_advertiser()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdAdvertiserDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_advertiser:
            user.remove_ad_advertiser()
        return HttpResponse("")



class AdWorkerAdminCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_ad_administrator_worker()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdWorkerAdminDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_ad_administrator_worker()
        return HttpResponse("")


class AdWorkerModerCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_ad_moderator_worker()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdWorkerModerDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_ad_moderator_worker()
        return HttpResponse("")


class AdWorkerEditorCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_ad_editor_worker()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdWorkerEditorDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_ad_editor_worker()
        return HttpResponse("")


class AdWorkerAdvertiserCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_ad_advertiser_worker()
            return HttpResponse("")
        else:
            return HttpResponse("")

class AdWorkerAdvertiserDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_ad_advertiser_worker()
        return HttpResponse("")
