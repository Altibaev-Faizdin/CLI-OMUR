from modeltranslation.translator import register, TranslationOptions
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
    WhyUs,
    ClinicHistory,
    Event,
)

@register(TherapyPage)
class TherapyPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(PopularService)
class PopularServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description')

@register(TherapyService)
class TherapyServiceTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(PatientTip)
class PatientTipTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(VideoMaterial)
class VideoMaterialTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(RecommendedSpecialist)
class RecommendedSpecialistTranslationOptions(TranslationOptions):
    fields = ('full_name', 'specialty')

@register(PreparationArticle)
class PreparationArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

@register(ServiceCategory)
class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("name", "description")

@register(Specialist)
class SpecialistTranslationOptions(TranslationOptions):
    fields = ("full_name", "specialization")

@register(ClinicLeader)
class ClinicLeaderTranslationOptions(TranslationOptions):
    fields = ("full_name", "position", "description")


@register(AboutClinic)
class AboutClinicTranslationOptions(TranslationOptions):
    fields = ("mission", "values")


@register(ClinicHistory)
class ClinicHistoryTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(WhyUs)
class WhyUsTranslationOptions(TranslationOptions):
    fields = ("title", "description")