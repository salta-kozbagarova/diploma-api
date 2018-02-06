from modeltranslation.translator import translator, TranslationOptions
from .models import CarBody
from django.utils.translation import gettext_lazy as _

class CarBodyTranslationOptions(TranslationOptions):
    fields = ('title',)
    fallback_values = _('-- sorry, no translation provided --')
    required_languages = ('ru', 'en')

translator.register(CarBody, CarBodyTranslationOptions)
