from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class AuctionBaseModel(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related", default=None, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='+', default=None, null=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    is_active = models.BooleanField(_('Is Active'), default=True)
    is_deleted = models.BooleanField(_('Is Deleted'), default=False)

    class Meta:
        abstract = True
