from django.db import models
from auction_api.common.models import AuctionBaseModel

# Create your models here.
class Color(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def natural_key(self):
        return (self.title)

class Product(AuctionBaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name="+", default=None, null=True)

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/products/<child_class_name>/<filename>
    folder_name = instance._meta.app_label.lower()
    return 'products/{0}/{1}'.format(folder_name, filename)

class ProductImage(AuctionBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", default=0)
    image = models.ImageField(upload_to=user_directory_path, null=True, default=None)
    is_main = models.BooleanField(default=False)
