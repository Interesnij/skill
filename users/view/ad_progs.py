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
