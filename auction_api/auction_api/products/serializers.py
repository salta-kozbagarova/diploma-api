from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, ProductImage, Color

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('url', 'id', 'name', 'description',
                  'productimage_related')

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = ProductImage
        fields = ('url', 'id', 'product', 'image')

class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ('url', 'id', 'title')
