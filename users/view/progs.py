from django.views import View
from users.models import User
from users.model.list import Subscribe
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from logs.models import UserWorkerLog, UserManageCreatorLog


class UserBanCreate(View):
    def get(self,request,*args,**kwargs):
        self.user = User.objects.get(pk=self.kwargs["pk"])
        request.user.block_user_with_pk(self.user.pk)
        return HttpResponse('')


class UserUnbanCreate(View):
    def get(self,request,*args,**kwargs):
        self.user = User.objects.get(pk=self.kwargs["pk"])
        request.user.unblock_user_with_pk(self.user.pk)
        return HttpResponse('')


class UserAdView(View):
    def get(self,request,*args,**kwargs):
        from stst.models import AdNumbers

        if request.user.is_authenticated:
            pk = self.kwargs["pk"]
            try:
                obj = AdNumbers.objects.get(user=request.user.pk, ad=pk)
                return HttpResponse('')
            except:
                obj = AdNumbers.objects.create(user=request.user.pk, ad=pk)
                return HttpResponse('')
        else:
            return HttpResponse('')


class PhoneVerify(View):
    def get(self,request,*args,**kwargs):
        from common.model.other import PhoneCodes
        from users.models import User

        code = self.kwargs["code"]
        _phone = self.kwargs["phone"]
        phone = request.user.get_last_location().phone + _phone
        try:
            obj = PhoneCodes.objects.get(code=code, phone=phone)
        except:
            obj = None
        if obj:
            user = User.objects.get(pk=request.user.pk)
            user.is_phone_verified=True
            user.phone=obj.phone
            user.save()
            obj.delete()
            data = 'ok'
            response = render(request,'generic/response/phone.html',{'response_text':data})
            return response
        else:
            data = 'Код подтверждения неверный. Проверьте, пожалуйста, номер, с которого мы Вам звонили. Последние 4 цифры этого номера и есть код подтверждения, который нужно ввести с поле "Последние 4 цифры". Если не можете найти номер, нажмите на кнопку "Перезвонить повторно".'
            response = render(request,'generic/response/phone.html',{'response_text':data})
            return response


class PhoneSend(View):
    def get(self,request,*args,**kwargs):
        import json, requests
        from common.model.other import PhoneCodes
        from users.models import User

        text = ""
        if request.user.is_phone_verified:
            return HttpResponse("")
        else:
            _phone = self.kwargs["phone"]
            if len(_phone) > 8:
                phone = request.user.get_last_location().phone + _phone
                try:
                    user = User.objects.get(phone=phone)
                    data = 'Пользователь с таким номером уже зарегистрирован. Используйте другой номер или напишите в службу поддержки, если этот номер Вы не использовали ранее.'
                    response = render(request,'generic/response/phone.html',{'response_text':data})
                    return response
                except:
                    response = requests.get(url="https://api.ucaller.ru/v1.0/initCall?service_id=12203&key=GhfrKn0XKAmA1oVnyEzOnMI5uBnFN4ck&phone=" + phone)
                    data = response.json()
                    PhoneCodes.objects.create(phone=phone, code=data['code'])
                    data = 'Мы Вам звоним. Последние 4 цифры нашего номера - код подтверждения, который нужно ввести в поле "Последние 4 цифры" и нажать "Подтвердить"'
                    response = render(request,'generic/response/code_send.html',{'response_text':data})
                    return response
            else:
                data = 'Введите, пожалуйста, корректное количество цифр Вашего телефона'
                response = render(request,'generic/response/phone.html',{'response_text':data})
                return response


class AddSubscribe(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user != user and not request.user.is_blocked_with_user_with_id(user_id=user.pk):
            Subscribe.objects.create(adding_user=request.user, added_user=user)
            return HttpResponse('')
        else:
            return HttpResponse('')


class UnSubscribe(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        try:
            subscribe = Subscribe.objects.get(adding_user=request.user, added_user=user)
            subscribe.delete()
            return HttpResponse('')
        except:
            return HttpResponse('')


class UserAdminCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_administrator:
            user.add_user_administrator()
            UserWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен админ пользователей')
            return HttpResponse("")
        else:
            return HttpResponse("")

class UserAdminDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_administrator:
            user.remove_user_administrator()
            UserWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален админ пользователей')
        return HttpResponse("")


class UserModerCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_moderator:
            user.add_user_moderator()
            UserWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен модератор пользователей')
            return HttpResponse("")
        else:
            return HttpResponse("")

class UserModerDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_moderator:
            user.remove_user_moderator()
            UserWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален модератор пользователей')
        return HttpResponse("")


class UserEditorCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_editor:
            user.add_user_editor()
            UserWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен редактор пользователей')
            return HttpResponse("")
        else:
            return HttpResponse("")

class UserEditorDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_editor:
            user.remove_user_editor()
            UserWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален редактор пользователей')
        return HttpResponse("")


class UserAdvertiserCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_advertiser:
            user.add_user_advertiser()
            UserWorkerLog.objects.create(manager=request.user, user=user, action_type='Добавлен рекламодатель пользователей')
            return HttpResponse("")
        else:
            return HttpResponse("")

class UserAdvertiserDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser and request.user.is_can_work_ad_advertiser:
            user.remove_user_advertiser()
            UserWorkerLog.objects.create(manager=request.user, user=user, action_type='Удален рекламодатель пользователей')
        return HttpResponse("")



class UserWorkerAdminCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_user_administrator_worker()
            UserManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель админов пользователей')
            return HttpResponse("")
        else:
            return HttpResponse("")

class UserWorkerAdminDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_user_administrator_worker()
            UserManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель админов пользователей')
        return HttpResponse("")


class UserWorkerModerCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_user_moderator_worker()
            return HttpResponse("")
            UserManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель модераторов пользователей')
        else:
            return HttpResponse("")

class UserWorkerModerDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_user_moderator_worker()
            UserManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель модераторов пользователей')
        return HttpResponse("")


class UserWorkerEditorCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_user_editor_worker()
            UserManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель редакторов пользователей')
            return HttpResponse("")
        else:
            return HttpResponse("")

class UserWorkerEditorDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_user_editor_worker()
            UserManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель редакторов пользователей')
        return HttpResponse("")


class UserWorkerAdvertiserCreate(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.add_user_advertiser_worker()
            UserManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Добавлен создатель рекламодателей пользователей')
            return HttpResponse("")
        else:
            return HttpResponse("")

class UserWorkerAdvertiserDelete(View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.is_superuser:
            user.remove_user_advertiser_worker()
            UserManageCreatorLog.objects.create(manager=request.user, user=user, action_type='Удален создатель рекламодателей пользователей')
        return HttpResponse("")
