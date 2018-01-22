from django.db import models
from django.conf import settings
import datetime

class AuctionBaseModel(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related", default=0)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         self.created_by = datetime.datetime.now()
    #     super(AuctionBaseModel, self).save(*args, **kwargs)
