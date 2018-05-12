from django.db import models

class CarMakeManager(models.Manager):
    def get_by_natural_key(self, code):
        return self.get(code=code)

class CarModelManager(models.Manager):
    def get_by_natural_key(self, code):
        return self.get(code=code)

class CarBodyManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)

class TransmissionManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)

class CarManager(models.Manager):

    def create_with_image(self, **data):
        car_model = apps.get_model('transports', 'Car')
        image_model = apps.get_model('transports', 'TransportImage')
        images = data.pop('image')
        car = car_model(**data)
        car.save()
        main_is_set=False
        for image in images:
            transport_image = image_model(product=car, image=image, is_main=not main_is_set)
            if not main_is_set:
                main_is_set = True
            transport_image.save()
        return car
