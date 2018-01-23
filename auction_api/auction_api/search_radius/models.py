from django.db import models

# Create your models here.
class SearchRadius(models.Model):

    METRIC_CHOICES = (
        ('км', 'км'),
    )

    radius = models.IntegerField()
    metric = models.CharField(choices=METRIC_CHOICES, max_length=255)
