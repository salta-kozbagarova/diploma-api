from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from auction_api.common.models import AuctionBaseModel
from django.conf import settings
from auction_api.administrative_division.models import AdministrativeDivision

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/users/<filename>
    return 'users/{0}'.format(filename)

@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    addresses = models.ManyToManyField(AdministrativeDivision, through='UserAddress',
                                          through_fields=('user', 'administrative_division'))
    photo = models.ImageField(upload_to=user_directory_path, null=True, default=None)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

class UserAddress(AuctionBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    administrative_division = models.ForeignKey(AdministrativeDivision, on_delete=models.CASCADE, default=None)

class UserPhone(AuctionBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, related_name='phonenumbers')
    phone = models.CharField(max_length=255, unique=True, null=True, blank=True, default=None)
    is_main = models.BooleanField(default=False)
