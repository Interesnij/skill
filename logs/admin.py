from django.contrib import admin
from logs.models import (
                            AdManageLog,
                            SkillManageLog,
                            AnketaManageLog,
                            UserManageLog,
                            AdWorkerLog,
                            SkillWorkerLog,
                            AnketaWorkerLog,
                            UserWorkerLog,
                        )


admin.site.register(AdManageLog)
admin.site.register(SkillManageLog)
admin.site.register(AnketaManageLog)
admin.site.register(UserManageLog)
admin.site.register(AdWorkerLog)
admin.site.register(SkillWorkerLog)
admin.site.register(AnketaWorkerLog)
admin.site.register(UserWorkerLog)
