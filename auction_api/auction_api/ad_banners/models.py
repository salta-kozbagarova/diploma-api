from django.db import models
from auction_api.common.models import AuctionBaseModel
from django.utils.translation import gettext_lazy as _

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/ad_banners/<filename>
    root_folder = instance._meta.app_label.lower()
    return '{0}/{1}'.format(root_folder, filename)

class AdBanner(AuctionBaseModel):
    name = models.CharField(_('Advertisement Banner'), max_length=255)
    image = models.ImageField(_('Image'), upload_to=user_directory_path)
