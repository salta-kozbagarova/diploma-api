from django.db import models

# Create your models here.
class Language(models.Model):
    code = models.CharField(max_length=255, unique=True)
    is_default = models.BooleanField(default=False)

    def natural_key(self):
        return (self.code,)
