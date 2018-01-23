from django.db import models
from .managers import AdministrativeLevelManager, AdministrativeDivisionManager

# Create your models here.
class AdministrativeLevel(models.Model):
    objects = AdministrativeLevelManager()
    name = models.CharField(max_length=255, unique=True)

    def natural_key(self):
        return (self.name,)

class AdministrativeDivision(models.Model):
    objects = AdministrativeDivisionManager()

    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True)
    administrative_level = models.ForeignKey(AdministrativeLevel, on_delete=models.PROTECT, default=None, null=True)

    def natural_key(self):
        return (self.name,self.administrative_level_id)

    class Meta:
        unique_together = ('name', 'administrative_level')
