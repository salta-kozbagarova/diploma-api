from django.db import models
from auction_api.common.models import AuctionBaseModel

# Create your models here.
class Product(AuctionBaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/products/<child_class_name>/<filename>
    folder_name = instance.__class__.__name__
    folder_name = folder_name[0:folder_name.index('Image')].lower()
    return 'products/{0}/{1}'.format(folder_name, filename)

class ProductImage(AuctionBaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related", default=0)
    image = models.ImageField(upload_to=user_directory_path)
