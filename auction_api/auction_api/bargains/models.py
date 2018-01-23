from django.db import models
from auction_api.categories.models import Category
from auction_api.common.models import AuctionBaseModel

class BargainType(AuctionBaseModel):
    name = models.TextField()

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/bargains/<filename>
    return 'bargains/{0}'.format(filename)

class Bargain(AuctionBaseModel):
    end_date = models.DateTimeField()
    bargain_type = models.ForeignKey(BargainType, on_delete=models.CASCADE, default=0)
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=user_directory_path)

    seen = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)

    class Meta:
        ordering = ('updated_at',)
