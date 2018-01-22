from django.db import models
from auction_api.common.models import AuctionBaseModel

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/categories/<category_name>/<filename>
    return 'categories/{0}/{1}'.format(instance.name, filename)

class CategoryManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Category(AuctionBaseModel):
    objects = CategoryManager()

    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to=user_directory_path)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True)
