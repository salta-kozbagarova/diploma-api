from django.db import models
from .managers import AdministrativeLevelManager, AdministrativeDivisionManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class AdministrativeLevel(models.Model):
    objects = AdministrativeLevelManager()
    name = models.CharField(_('Administrative Level'), max_length=255, unique=True)

    def natural_key(self):
        return (self.name,)

class AdministrativeDivision(models.Model):
    objects = AdministrativeDivisionManager()

    name = models.CharField(_('Administrative Division'), max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, related_name='subdivisions')
    administrative_level = models.ForeignKey(AdministrativeLevel, on_delete=models.PROTECT, default=None, null=True)

    def natural_key(self):
        return (self.name,self.administrative_level.name)

    def __unicode__(self):
        return self.name

    def get_full_address(self):
        if self.parent:
            full_name = self.parent.get_full_address()
            return '{0}, {1}'.format(full_name, self.name)
        else:
            return self.name

    class Meta:
        unique_together = ('name', 'administrative_level')
