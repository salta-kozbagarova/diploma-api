from django.db import models
from auction_api.common.models import AuctionBaseModel
from .managers import CategoryManager
from django.template.defaultfilters import slugify

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/categories/<root_category_name>/<filename>
    folder_name = instance.root_parent.code
    return 'categories/{0}/{1}'.format(folder_name, filename)

class Category(AuctionBaseModel):
    objects = CategoryManager()
    code = models.SlugField(unique=True, null=True, default=None)
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to=user_directory_path)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, related_name='subcategories')

    @property
    def root_parent(self):
        if self.parent is not None:
            category = self.parent
            while category.parent is not None:
                category = category.parent
            return category
        else:
            self.parent

    def save(self, *args, **kwargs):
        if not self.id:
            self.code = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
