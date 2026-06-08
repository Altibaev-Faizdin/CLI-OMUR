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
    FAQ
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