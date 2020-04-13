from django.contrib import admin
from users.model.profile import UserProfile, IPUser, OneUserLocation, TwoUserLocation, ThreeUserLocation
from users.model.list import Favourites, ChatAd, Subscribe, Guest
from django.conf import settings


admin.site.register(settings.AUTH_USER_MODEL)

admin.site.register(UserProfile)
admin.site.register(IPUser)
admin.site.register(OneUserLocation)
admin.site.register(TwoUserLocation)
admin.site.register(ThreeUserLocation)

admin.site.register(Favourites)
admin.site.register(ChatAd)
admin.site.register(Subscribe)
admin.site.register(Guest)
