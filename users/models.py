import uuid
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied
from django.db import models



class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False, verbose_name='Почта подтверждена')
    is_phone_verified = models.BooleanField(default=False, verbose_name='Телефон подтвержден')
    is_deleted = models.BooleanField(verbose_name="Удален", default=False, )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="uuid")
    last_activity= models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Активность')
    phone = models.CharField(max_length=17, unique=True, verbose_name='Телефон')
    is_deleted = models.BooleanField(default=False, verbose_name='Пользователь удален')
    is_blocked = models.BooleanField(default=False, verbose_name='Пользователь заблокирован')
    USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def get_full_name(self):
        return  str(self.first_name) + " " + str(self.last_name)

    def get_online(self):
        from datetime import datetime, timedelta

        now = datetime.now()
        onl = self.last_activity + timedelta(minutes=3)
        if now < onl:
            return True
        else:
            return False

    def get_template_user(self, folder, template, request):
        import re
        from stst.models import UserNumbers

        if self.pk == request.user.pk:
            if not request.user.is_phone_verified:
                template_name = "main/phone_verification.html"
            else:
                template_name = folder + "my_" + template
        elif request.user.pk != self.pk and request.user.is_authenticated:
            if not request.user.is_phone_verified:
                template_name = "main/phone_verification.html"
            elif request.user.is_blocked_with_user_with_id(user_id=self.pk):
                template_name = folder + "block_" + template
            elif request.user.is_adding_user_with_id(user_id=self.pk):
                template_name = folder + "adding_" + template
            elif request.user.is_added_user_with_id(user_id=self.pk):
                template_name = folder + "added_" + template
            elif request.user.is_deleted:
                template_name = "main/deleted_page.html"
            elif request.user.is_blocked:
                template_name = "main/blocked_page.html"
        elif request.user.is_anonymous:
            template_name = folder + "anon_" + template

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            template_name = "mob_" + template_name
            if request.user.is_authenticated:
                UserNumbers.objects.create(visitor=request.user.pk, target=self.pk, platform=1)
        else:
            if request.user.is_authenticated:
                UserNumbers.objects.create(visitor=request.user.pk, target=self.pk, platform=0)
        return template_name

    def get_my_template(self, folder, template, request):
        import re
        if self.pk == request.user.pk:
            if not request.user.is_phone_verified:
                template_name = "main/phone_verification.html"
            elif request.user.is_deleted:
                template_name = "main/deleted_page.html"
            elif request.user.is_blocked:
                template_name = "main/blocked_page.html"
            elif request.user.is_anonymous:
                template_name = "main/anon_page.html"
            else:
                template_name = folder + template
        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            template_name = "mob_" + template_name
        return template_name

    def is_adding_user_with_id(self, user_id):
        return self.adding_user.filter(adding_user__id=user_id).exists()

    def is_added_user_with_id(self, user_id):
        return self.added_user.filter(added_user__id=user_id).exists()

    def unsubscribe_user(self, user):
        return self.unsubscribe_user_with_id(user.pk)

    def unsubscribe_user_with_id(self, user_id):
        from users.model.list import Subscribe

        check_not_can_follow_user_with_id(user=self, user_id=user_id)
        subscribe = Subscribe.objects.get(adding_user=self, added_user__id=user_id)
        subscribe.delete()

    def block_user_with_pk(self, pk):
        user = User.objects.get(pk=pk)
        return self.block_user_with_id(user_id=user.pk)

    def block_user_with_id(self, user_id):
        from users.model.list import UserBlock
        check_can_block_user_with_id(user=self, user_id=user_id)

        if self.is_adding_user_with_id(user_id=user_id):
            self.unsubscribe_user_with_id(user_id=user_id)

        user_to_block = User.objects.get(pk=user_id)
        if user_to_block.is_adding_user_with_id(user_id=self.pk):
            user_to_block.unsubscribe_user_with_id(self.pk)

        UserBlock.create_user_block(blocker_id=self.pk, blocked_user_id=user_id)
        return user_to_block

    def unblock_user_with_pk(self, pk):
        user = User.objects.get(pk=pk)
        return self.unblock_user_with_id(user_id=user.pk)

    def unblock_user_with_id(self, user_id):
        check_can_unblock_user_with_id(user=self, user_id=user_id)
        self.user_blocks.filter(blocked_user_id=user_id).delete()
        return User.objects.get(pk=user_id)

    def get_last_location(self):
        from users.model.profile import OneUserLocation, TwoUserLocation, ThreeUserLocation

        if self.user_ip.ip_3:
            return ThreeUserLocation.objects.get(user=self)
        elif self.user_ip.ip_2:
            return TwoUserLocation.objects.get(user=self)
        elif self.user_ip.ip_1:
            return OneUserLocation.objects.get(user=self)
        else:
            return "Местоположение не указано"

    def get_my_active_ads(self):
        from ad_posts.models import Ad

        ads_query = Q(creator_id=self.id, is_active=True, is_sold=False, is_deleted=False)
        ads = Ad.objects.filter(ads_query)
        return ads

    def get_my_noactive_ads(self):
        from ad_posts.models import Ad

        ads_query = Q(creator_id=self.id, is_active=False, is_sold=False, is_deleted=False)
        ads = Ad.objects.filter(ads_query)
        return ads

    def get_my_sold_ads(self):
        from ad_posts.models import Ad

        ads_query = Q(creator_id=self.id, is_active=False, is_sold=True, is_deleted=False)
        ads = Ad.objects.filter(ads_query)
        return ads

    def get_my_favorite_ads(self):
        from ad_posts.models import Ad

        favorites_query = Q(creator__favorites_user__user_id=self.id, is_active=True, is_sold=False, is_deleted=False)
        favorites_query.add(~Q(Q(creator__blocked_by_users__blocker_id=self.id) | Q(creator__user_blocks__blocked_user_id=self.id)), Q.AND)
        favorites = Ad.objects.filter(favorites_query)
        return favorites

    def get_my_subscribs(self):
        """Это те, кто на меня подписался"""

        subscribs_query = Q(adding_user__adding_user__id=self.id, is_deleted=False)
        subscribs_query.add(~Q(Q(blocked_by_users__blocker_id=self.id) | Q(user_blocks__blocked_user_id=self.id)), Q.AND)
        subscribs = User.objects.filter(subscribs_query)
        return subscribs

    def get_subscribs(self):
        """Это те, на кого я подписался"""

        subscribs_query = Q(added_user__added_user__id=self.id, is_deleted=False)
        subscribs_query.add(~Q(Q(blocked_by_users__blocker_id=self.id) | Q(user_blocks__blocked_user_id=self.id)), Q.AND)
        subscribs = User.objects.filter(subscribs_query)
        return subscribs

    def last_ads_for_russia(self):
        from ad_posts.models import Ad

        ads_query = Q(city__region__country__id=1, creator__is_blocked=False, is_deleted=False, is_active=True)
        ads = Ad.objects.filter(ads_query)
        return ads[:21]
