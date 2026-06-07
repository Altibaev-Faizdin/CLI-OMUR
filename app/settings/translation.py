from modeltranslation.translator import register, TranslationOptions
from app.settings.models import TherapyPage, PopularService, TherapyService

@register(TherapyPage)
class TherapyPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(PopularService)
class PopularServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description')

@register(TherapyService)
class TherapyServiceTranslationOptions(TranslationOptions):
    fields = ('title', )