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
    lat = models.FloatField(_('Latitude'), null=True)
    lon = models.FloatField(_('Longitude'), null=True)

    def natural_key(self):
        return (self.name,self.administrative_level.name)

    def __unicode__(self):
        return self.name

    @property
    def full_address(self):
        if self.parent:
            full_name = self.parent.full_address
            return '{0}, {1}'.format(full_name, self.name)
        else:
            return self.name

    @property
    def all_children_id(self):
        adms = self.subdivisions.all()
        if len(adms):
            child = []
            for adm in adms:
                child += adm.all_children_id
            child += [self.pk]
            return child
        else:
            return [self.pk]

    class Meta:
        unique_together = ('name', 'administrative_level')
