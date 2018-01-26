from modeltranslation.translator import translator, TranslationOptions
from .models import BargainType
from django.utils.translation import gettext_lazy as _

class BargainTypeTranslationOptions(TranslationOptions):
    fields = ('name',)
    fallback_values = _('-- sorry, no translation provided --')
    required_languages = ('ru', 'en')

translator.register(BargainType, BargainTypeTranslationOptions)
