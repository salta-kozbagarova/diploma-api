from django.db import models
from auction_api.categories.models import Category
from auction_api.common.models import AuctionBaseModel
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from auction_api.administrative_division.models import AdministrativeDivision
from .managers import BargainTypeManager
from auction_api.products.models import Product
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

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
    start_price = models.IntegerField(_('Start Price'))
    current_price = models.IntegerField(_('Current Price'))
    seen = models.IntegerField(_('Seen'))
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BargainBet',
                                          through_fields=('bargain', 'created_by'), related_name="bargains")
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BargainComment',
                                          through_fields=('bargain', 'created_by'), related_name="bargain_comments")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, related_name="bargains", null=True)
    address = models.ForeignKey(AdministrativeDivision, on_delete=models.SET_NULL, default=None, related_name="bargain_addresses", null=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, default=None, null=True)
    on_top = models.BooleanField(default=False)

    content_type = models.OneToOneField(ContentType, on_delete=models.CASCADE, default=None)
    object_id = models.PositiveIntegerField()
    bargained_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('-on_top','-updated_at',)

    def __str__(self):
        return '#{}: {}: {}'.format(self.pk, self.category, self.product)

class Bookmark(models.Model):
    """
    A bookmark consists of a URL, and 0 or more descriptive tags.
    """
    url = models.URLField()
    bargain = GenericRelation(Bargain)

class BargainBet(AuctionBaseModel):
    bargain = models.ForeignKey(Bargain, on_delete=models.CASCADE, default=None)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)

class BargainComment(AuctionBaseModel):
    bargain = models.ForeignKey(Bargain, on_delete=models.CASCADE, default=None)
    comment = models.TextField(_('Comment'))
