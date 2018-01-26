from django.db import models
from auction_api.common.models import AuctionBaseModel
from auction_api.bargains.models import Bargain

# Create your models here.
class Color(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def natural_key(self):
        return (self.title)

class Product(AuctionBaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name="+", default=None, null=True)
    bargain = models.ForeignKey(Bargain, on_delete=models.SET_NULL, related_name="products", default=None, null=True)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/products/<child_class_name>/<filename>
    folder_name = instance._meta.app_label.lower()
    return 'products/{0}/{1}'.format(folder_name, filename)

class ProductImage(AuctionBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="%(class)s_related", default=0)
    image = models.ImageField(upload_to=user_directory_path)
