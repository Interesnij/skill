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
