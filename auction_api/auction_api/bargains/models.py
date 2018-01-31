from django.db import models
from auction_api.categories.models import Category
from auction_api.common.models import AuctionBaseModel
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from auction_api.administrative_division.models import AdministrativeDivision
from .managers import BargainTypeManager
from django.utils import timezone

class BargainType(AuctionBaseModel):
    objects = BargainTypeManager()
    name = models.TextField(_('Bargain Type'), unique=True, null=True, default=None)

    class Meta:
        ordering = ('name',)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/bargains/<filename>
    root_folder = instance._meta.app_label.lower()
    category_folder = instance.category.root_parent.code
    return '{0}/{1}/{2}'.format(root_folder, category_folder, filename)

class Bargain(AuctionBaseModel):
    end_date = models.DateTimeField(_('End Date'), auto_now_add=True)
    bargain_type = models.ForeignKey(BargainType, on_delete=models.SET_NULL, default=None, null=True)
    start_price = models.DecimalField(_('Start Price'), max_digits=10, decimal_places=2)
    current_price = models.DecimalField(_('Current Price'), max_digits=10, decimal_places=2)
    name = models.CharField(_('Bargain Name'), max_length=255)
    description = models.TextField(_('Bargain Description'), default=None)
    image = models.ImageField(_('Image'), upload_to=user_directory_path)
    seen = models.IntegerField(_('Seen'))
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BargainBet',
                                          through_fields=('bargain', 'created_by'), related_name="bargains")
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BargainComment',
                                          through_fields=('bargain', 'created_by'), related_name="bargain_comments")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, related_name="bargains", null=True)
    address = models.ForeignKey(AdministrativeDivision, on_delete=models.SET_NULL, default=None, related_name="bargain_addresses", null=True)

    class Meta:
        ordering = ('updated_at',)

class BargainBet(AuctionBaseModel):
    bargain = models.ForeignKey(Bargain, on_delete=models.CASCADE, default=None)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)

class BargainComment(AuctionBaseModel):
    bargain = models.ForeignKey(Bargain, on_delete=models.CASCADE, default=None)
    comment = models.TextField(_('Comment'))
