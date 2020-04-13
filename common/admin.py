from django.contrib import admin
from common.model.votes import AdVotes
from common.model.other import PhoneCodes


class AdVotesAdmin(admin.ModelAdmin):
    list_display = (
        'vote',
        'user',
        #'parent',
    )

admin.site.register(AdVotes, AdVotesAdmin)
admin.site.register(PhoneCodes)
