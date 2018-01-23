from django.db import models

class CategoryManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)
