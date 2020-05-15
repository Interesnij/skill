from django.contrib import admin
from users.model.profile import (
                                    UserProfile,
                                    IPUser,
                                    OneUserLocation,
                                    TwoUserLocation,
                                    ThreeUserLocation,
                                    UserAdStaff,
                                    UserSkillStaff,
                                    UserAnketaStaff,
                                    CanAddStaffAdUser,
                                    CanAddStaffSkillUser,
                                    CanAddStaffAnketaUser,
                                    CanAddStaffUser,
                                    UserStaff
                                )
from users.model.list import ChatAd, Subscribe, Guest, UserBlock
from django.conf import settings
from users.models import User


admin.site.register(User)

admin.site.register(UserProfile)
admin.site.register(IPUser)
admin.site.register(OneUserLocation)
admin.site.register(TwoUserLocation)
admin.site.register(ThreeUserLocation)

admin.site.register(UserAdStaff)
admin.site.register(UserSkillStaff)
admin.site.register(UserAnketaStaff)
admin.site.register(UserStaff)

admin.site.register(CanAddStaffAdUser)
admin.site.register(CanAddStaffSkillUser)
admin.site.register(CanAddStaffAnketaUser)
admin.site.register(CanAddStaffUser)

admin.site.register(ChatAd)
admin.site.register(Subscribe)
admin.site.register(Guest)
admin.site.register(UserBlock)
