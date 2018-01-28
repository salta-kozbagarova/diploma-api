from django.db import models
from auction_api.products.models import Product, ProductImage

# Create your models here.
class Art(models.Model):
    author = models.CharField(max_length=255)
    published = models.DateField()

    class Meta:
        abstract = True

class Painting(Art, Product):
    material = models.CharField(max_length=255)
