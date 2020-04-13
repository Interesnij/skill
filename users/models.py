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

    def get_template_main(self, folder, template, request):
        import re

        if self.is_authenticated and not self.is_deleted:
            template_name = folder + template
        elif self.is_authenticated and self.is_deleted:
            template_name = "generic/user_deleted.html"
        else:
            template_name = folder + "anon_" + template

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
