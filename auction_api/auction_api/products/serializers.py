from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, ProductImage

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('url', 'id', 'name', 'description',
                  'products_productimage_related')

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('url', 'id', 'product_id', 'image')
