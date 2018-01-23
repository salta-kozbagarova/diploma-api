from django.db import models
from auction_api.products.models import Product, ProductImage
import datetime
from .managers import CarMakeManager

# Create your models here.
class Transport(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    manifacture_year = models.DateField()
    engine_volume = models.FloatField()
    mileage = models.CharField(max_length=255)
    customs_cleared = models.BooleanField()

    class Meta:
        abstract = True

class TransportImage(ProductImage):
    pass

class CarMake(models.Model):
    objects = CarMakeManager()

    code = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)

    def natural_key(self):
        return (self.code,)

class CarModel(models.Model):
    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="%(class)s", default=None)

    def natural_key(self):
        return (self.code,)

    class Meta:
        unique_together = ("make", "code")

class CarBody(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def natural_key(self):
        return (self.title)

class Transmission(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def natural_key(self):
        return (self.title)

class Car(Transport, Product):
    YEAR_CHOICES = ((r, r) for r in range(1960, datetime.date.today().year + 1))

    STEERING_LEFT = 'слева'
    STEERING_RIGHT = 'справа'
    STEERING_CHOICES = ((STEERING_LEFT, 'слева'), (STEERING_RIGHT, 'справа'))

    STATE_IN_ACTION = 'на ходу'
    STATE_NOT_IN_ACTION = 'не на ходу'
    STATE_EMERGENCY = 'аварийный'
    STATE_CHOICES = (
        (STATE_IN_ACTION, 'на ходу'),
        (STATE_NOT_IN_ACTION, 'не на ходу'),
        (STATE_EMERGENCY, 'аварийный')
    )

    DRIVE_FRONT_WHEEL = 'передний'
    DRIVE_REAR_WHEEL = 'задний'
    DRIVE_ALL_WHEEL = 'полный'
    DRIVE_CHOICES = (
        (DRIVE_FRONT_WHEEL, 'передний'),
        (DRIVE_REAR_WHEEL, 'задний'),
        (DRIVE_ALL_WHEEL, 'полный')
    )

    make = models.ForeignKey(CarMake, on_delete=models.DO_NOTHING, related_name="+", default=None)
    model = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING, related_name="+", default=None)
    body = models.ForeignKey(CarBody, on_delete=models.DO_NOTHING, related_name="+", default=None)
    manifacture_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    engine_volume = models.FloatField()
    transmission = models.ForeignKey(Transmission, on_delete=models.DO_NOTHING, related_name="+", default=None, null=True)
    mileage = models.CharField(max_length=255)
    steering = models.CharField(max_length=255, choices=STEERING_CHOICES, default=STEERING_LEFT)
    metallic = models.BooleanField(default=False)
    customs_cleared = models.BooleanField()
    state = models.CharField(max_length=255, choices=STATE_CHOICES)
    drive = models.CharField(max_length=255, choices=DRIVE_CHOICES)
