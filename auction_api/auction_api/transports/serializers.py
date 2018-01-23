from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Car, CarMake, CarModel, TransportImage, CarBody, Transmission

class CarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Car
        fields = ('url', 'id', 'name', 'description', 'make', 'model', 'body', 'manifacture_year', 'engine_volume',
                  'transmission', 'mileage', 'steering', 'color', 'metallic', 'customs_cleared', 'state', 'drive',
                  'productimage_related')

class CarMakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarMake
        fields = ('url', 'id', 'code', 'title')

class CarModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarModel
        fields = ('url', 'id', 'code', 'title', 'make')

class CarBodySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarBody
        fields = ('url', 'id', 'title')

class TransmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transmission
        fields = ('url', 'id', 'title')

class TransportImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TransportImage
        fields = ('url', 'id', 'product', 'image')
