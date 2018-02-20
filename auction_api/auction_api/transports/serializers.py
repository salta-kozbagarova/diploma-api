from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Car, CarMake, CarModel, TransportImage, CarBody, Transmission
from django.db import models
from auction_api.products.serializers import ProductImageSerializer
from collections import OrderedDict

class CarListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        cars = [Car(**item) for item in validated_data]
        return Car.objects.bulk_create(cars)

class ProductImageField(serializers.RelatedField):
    # image = serializers.ImageField()
    def to_representation(self, value):
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(value.image.url)
        return value.image.url

    def to_internal_value(self, data):
        try:
            # `UploadedFile` objects should have name and size attributes.
            file_name = data.name
            file_size = data.size
        except AttributeError:
            self.fail('invalid')

        if not file_name:
            self.fail('no_name')
        if not self.allow_empty_file and not file_size:
            self.fail('empty')
        if self.max_length and len(file_name) > self.max_length:
            self.fail('max_length', max_length=self.max_length, length=len(file_name))

        # Image validation is a bit grungy, so we'll just outright
        # defer to Django's implementation so we don't need to
        # consider it, or treat PIL as a test dependency.
        file_object = data
        django_field = self._DjangoImageField()
        django_field.error_messages = self.error_messages
        return django_field.clean(file_object)

class CarSerializer(serializers.HyperlinkedModelSerializer):
    # productimage_related = serializers.ListField(
    #     child=serializers.ImageField()
    # )
    #productimage_related = serializers.ImageField()
    # productimage_related = ProductImageSerializer(many=True, required=False)

    #testimg = serializers.ImageField(source='productimage_related.image')
    # productimage_related = ProductImageField(queryset=TransportImage.objects.all(),many=True)
    class Meta:
        model = Car
        list_serializer_class = CarListSerializer
        fields = ('url', 'id', 'name', 'description', 'make', 'model', 'body', 'manifacture_year', 'engine_volume',
                  'transmission', 'mileage', 'steering', 'color', 'metallic', 'customs_cleared', 'state', 'drive',
                  'productimage_related')

    # def create(self, validated_data):
    #     print(validated_data)
    #     carimage = validated_data.pop('productimage_related')
    #     print(validated_data)
    #     car = Car.objects.create(**validated_data)
    #     newdata = []
    #     for item in carimage:
    #         #TransportImage.objects.create(product=car, image=item)
    #         dict = {}
    #         dict['product'] = car
    #         dict['image'] = item
    #         newdata.append(dict)
    #     print(newdata)
    #     # iterable = newdata.all() if isinstance(newdata, models.Manager) else newdata
    #     # print(iterable)
    #     # for item in iterable:
    #     #     print(item)
    #     # TransportImageSerializer(many=True, data=carimage)
    #     #TransportImageSerializer.create(TransportImageSerializer(many=True), validated_data=newdata)
    #     # TransportImageListSerializer.create(TransportImageListSerializer(), validated_data=newdata)
    #     # TransportImage.objects.create(product=car, image=carimage)
    #     return car

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

# class TransportImageListSerializer(serializers.ListSerializer):
#
#     class Meta:
#         model = TransportImage
#         fields = '__all__'
#
#     def create(self, validated_data):
#         print('we got here')
#         images = [TransportImage(**item) for item in validated_data]
#         return TransportImage.objects.bulk_create(images)

class TransportImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TransportImage
        # list_serializer_class = TransportImageListSerializer
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
