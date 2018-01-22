from django.db import models
from auction_api.products.models import Product, ProductImage

# Create your models here.
class Transport(Product):
    mark = models.CharField(max_length=255)
    rear_type = models.TextField()

class TransportImage(ProductImage):
    pass
