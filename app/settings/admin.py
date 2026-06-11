from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline
from app.settings import translation

from app.settings.models import (
    TherapyPage,
    PopularService,
    TherapyService,
    PatientTip,
    VideoMaterial,
    RecommendedSpecialist,
    PreparationArticle,
    PreparationArticleImage,
    FAQ,
    ServiceCategory,
    Service,
    Specialist
)

class ServiceInline(TranslationTabularInline):
    model = Service
    extra = 0

class PreparationArticleImageInline(admin.TabularInline):
    model = PreparationArticleImage
    extra = 1

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

@admin.register(PatientTip)
class PatientTipAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'description', 'image', 'button_text', 'button_url')
    search_fields = ('title',)

@admin.register(VideoMaterial)
class VideoMaterialAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'description', 'thumbnail', 'video_url')
    search_fields = ('title',)

@admin.register(RecommendedSpecialist)
class RecommendedSpecialistAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'full_name', 'specialty', 'photo', 'profile_url')
    search_fields = ('full_name',)

@admin.register(PreparationArticle)
class PreparationArticleAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ('title',)
    inlines = [PreparationArticleImageInline]

@admin.register(FAQ)
class FAQAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'question', 'answer')
    search_fields = ('question',)

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(TabbedTranslationAdmin):
    list_display = ("name", "slug", "order")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ServiceInline]


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ("name", "category", "is_active", "order", "created_at")
    list_filter = ("category", "is_active")
    list_editable = ("is_active", "order")
    search_fields = ("name",)
    readonly_fields = ("created_at",)


@admin.register(Specialist)
class SpecialistAdmin(TabbedTranslationAdmin):
    list_display = ("full_name", "specialization", "experience", "order")
    list_editable = ("order",)
    search_fields = ("full_name", "specialization")
