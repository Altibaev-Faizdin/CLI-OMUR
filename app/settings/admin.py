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
    Specialist,
    ClinicLeader,
    AboutClinic,
    AboutClinicImage,
    ClinicHistory,
    ClinicHistoryImage,
    Event,
    EventImage,
    WhyUs,
)


class ServiceInline(TranslationTabularInline):
    model = Service
    extra = 0


class PreparationArticleImageInline(admin.TabularInline):
    model = PreparationArticleImage
    extra = 1


class AboutClinicImageInline(admin.TabularInline):
    model = AboutClinicImage
    extra = 1


class ClinicHistoryImageInline(admin.TabularInline):
    model = ClinicHistoryImage
    extra = 1


class EventImageInline(admin.TabularInline):
    model = EventImage
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
    list_display = ("name", "slug", "service_type", "order")
    list_filter = ("service_type",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ServiceInline]


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ("name", "category", "order", "created_at")
    list_filter = ("category",)
    list_editable = ("order",)
    search_fields = ("name",)
    readonly_fields = ("created_at",)


@admin.register(Specialist)
class SpecialistAdmin(TabbedTranslationAdmin):
    list_display = ("full_name", "specialization", "specialist_type", "experience", "order")
    list_filter = ("specialist_type",)
    list_editable = ("order",)
    search_fields = ("full_name", "specialization")


@admin.register(ClinicLeader)
class ClinicLeaderAdmin(TabbedTranslationAdmin):
    list_display = ("full_name", "position")
    search_fields = ("full_name",)


@admin.register(AboutClinic)
class AboutClinicAdmin(TabbedTranslationAdmin):
    list_display = ("id", "mission", "values")
    inlines = [AboutClinicImageInline]


@admin.register(ClinicHistory)
class ClinicHistoryAdmin(TabbedTranslationAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
    search_fields = ("title",)
    inlines = [ClinicHistoryImageInline]


@admin.register(Event)
class EventAdmin(TabbedTranslationAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
    search_fields = ("title",)
    inlines = [EventImageInline]


@admin.register(WhyUs)
class WhyUsAdmin(TabbedTranslationAdmin):
    list_display = ("title", "description", "order")
    list_editable = ("order",)
    search_fields = ("title",)