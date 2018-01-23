from django.db import models
from auction_api.common.models import AuctionBaseModel
from .managers import CategoryManager

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/categories/<root_category_name>/<filename>
    folder_name = instance.root_parent.name
    return 'categories/{0}/{1}'.format(folder_name, filename)

class Category(AuctionBaseModel):
    objects = CategoryManager()
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to=user_directory_path)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True)

    # @property
    # def name(self):
    #     category = CategoryI18n.objects.get(category__pk=self.pk, language__is_default=1)
    #     if category:
    #         return category.name
    #     else:
    #         return ''

    @property
    def root_parent(self):
        if self.parent is not None:
            category = self.parent
            while category.parent is not None:
                category = category.parent
            return category
        else:
            self.parent

class CategoryI18n(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True, related_name="translations")
    language = models.ForeignKey('base.language', on_delete=models.CASCADE, default=None, null=True, related_name="+")
    name = models.CharField(max_length=255, unique=True)
