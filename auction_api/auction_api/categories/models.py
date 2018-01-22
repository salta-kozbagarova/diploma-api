from django.db import models
from auction_api.common.models import AuctionBaseModel

# Create your models here.

class Category(AuctionBaseModel):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, default=None)
