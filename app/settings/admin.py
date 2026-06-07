from django.contrib import admin

from .models import (
    TherapyPage,
    PopularService,
    TherapyService,
    CallbackRequest
)


admin.site.register(TherapyPage)
admin.site.register(PopularService)
admin.site.register(TherapyService)
admin.site.register(CallbackRequest)
