from modeltranslation.translator import register, TranslationOptions
from .models import TherapyPage, PopularService, TherapyService

@register(TherapyPage)
class TherapyPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(PopularService)
class PopularServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(TherapyService)
class TherapyServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')