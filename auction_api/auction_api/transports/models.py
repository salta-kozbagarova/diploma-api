from django.db import models
from auction_api.products.models import Product, ProductImage
import datetime
from .managers import CarMakeManager, CarManager, CarBodyManager, CarModelManager, TransmissionManager
from django.utils.translation import gettext_lazy as _

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
    code = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    objects = CarMakeManager()

    def natural_key(self):
        return (self.code,)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class CarModel(models.Model):
    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="%(class)s", default=None)
    objects = CarModelManager()

    def natural_key(self):
        return (self.code,)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("make", "code")
        ordering = ('title',)

class CarBody(models.Model):
    title = models.CharField(max_length=255, unique=True)
    objects = CarBodyManager()

    def natural_key(self):
        return (self.title,)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Transmission(models.Model):
    title = models.CharField(max_length=255, unique=True)
    objects = TransmissionManager()

    def natural_key(self):
        return (self.title,)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

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

    objects = CarManager()

    make = models.ForeignKey(CarMake, on_delete=models.DO_NOTHING, related_name="+", default=None, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING, related_name="+", default=None, null=True)
    body = models.ForeignKey(CarBody, on_delete=models.DO_NOTHING, related_name="+", default=None, null=True)
    manifacture_year = models.IntegerField(_('Manifacture Year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)
    engine_volume = models.FloatField(_('Engine Volume'), null=True)
    transmission = models.ForeignKey(Transmission, on_delete=models.DO_NOTHING, related_name="+", default=None, null=True)
    mileage = models.CharField(_('Mileage'), max_length=255, null=True)
    steering = models.CharField(_('Steering'), max_length=255, choices=STEERING_CHOICES, default=STEERING_LEFT, null=True)
    metallic = models.BooleanField(_('Metallic'), default=False)
    customs_cleared = models.BooleanField(_('Customs cleared'), default=False)
    state = models.CharField(_('State'), max_length=255, choices=STATE_CHOICES, null=True)
    drive = models.CharField(_('Drive'), max_length=255, choices=DRIVE_CHOICES, null=True)
