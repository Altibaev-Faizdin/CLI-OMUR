from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from app.settings.models import (
    TherapyPage,
    PopularService,
    TherapyService,
)

from app.settings import translation

@admin.register(TherapyPage)
class TherapyPageAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'description', 'banner_image')
    search_fields = ('id', 'title')


@admin.register(PopularService)
class PopularServiceAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'short_description', 'order')
    search_fields = ('title',)


@admin.register(TherapyService)
class TherapyServiceAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'order')
    search_fields = ('title',)
