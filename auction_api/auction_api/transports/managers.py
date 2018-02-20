from django.db import models
from django.apps import apps

class CarMakeManager(models.Manager):
    def get_by_natural_key(self, code):
        return self.get(code=code)

class CarManager(models.Manager):

    def create_with_image(self, **data):
        car_model = apps.get_model('transports', 'Car')
        image_model = apps.get_model('transports', 'TransportImage')
        images = data.pop('image')
        car = car_model(**data)
        car.save()
        for image in images:
            transport_image = image_model(product=car, image=image)
            transport_image.save()
        return car
