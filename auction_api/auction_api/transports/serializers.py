from rest_framework import serializers
from .models import Car, CarMake, CarModel, TransportImage, CarBody, Transmission
from auction_api.products.serializers import ProductImageField
from django.conf import settings

class CarListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        cars = [Car(**item) for item in validated_data]
        return Car.objects.bulk_create(cars)

class CarSerializer(serializers.HyperlinkedModelSerializer):
    images = ProductImageField(
        queryset=TransportImage.objects.all(),
        many=True
    )
    # imagess = serializers.SerializerMethodField()

    class Meta:
        model = Car
        list_serializer_class = CarListSerializer
        fields = ('url', 'id', 'name', 'description', 'make', 'model', 'body', 'manifacture_year', 'engine_volume',
                  'transmission', 'mileage', 'steering', 'color', 'metallic', 'customs_cleared', 'state', 'drive',
                  'images')

    # def get_imagess(self, obj):
    #     request = self.context.get('request', None)
    #     if obj.images.count() is not 0:
    #         images = []
    #         for image in obj.images.all():
    #             url = image.image.url
    #             if request is not None:
    #                 images.append(request.build_absolute_uri(url))
    #             else:
    #                 images.append(url)
    #         return images
    #     print(request.build_absolute_uri(settings.IMAGE_PLACEHOLDER))
    #     return [request.build_absolute_uri('/'+settings.IMAGE_PLACEHOLDER)] if request is not None else [settings.IMAGE_PLACEHOLDER]

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

class CarFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    image = serializers.ListField(
        child=serializers.ImageField()
    )

    def create(self, validated_data):
        Car.objects.create_with_image(**validated_data)
        return validated_data
