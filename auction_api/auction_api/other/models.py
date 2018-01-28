from django.db import models
from auction_api.products.models import Product, ProductImage

# Create your models here.
class Other(models.Model):

    class Meta:
        abstract = True

class Item(Other, Product):
    material = models.CharField(max_length=255)
