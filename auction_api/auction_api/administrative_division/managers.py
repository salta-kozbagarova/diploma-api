from django.db import models

class AdministrativeLevelManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class AdministrativeDivisionManager(models.Manager):
    def get_by_natural_key(self, name, administrative_level_id):
        return self.get(name=name, administrative_level_id=administrative_level_id)
