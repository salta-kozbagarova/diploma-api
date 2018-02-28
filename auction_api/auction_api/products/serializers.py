from rest_framework import serializers
from .models import Product, ProductImage, Color

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = ProductImage
        fields = ('url', 'id', 'product', 'image', 'is_main')

class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ('url', 'id', 'title')

class ProductImageField(serializers.RelatedField):
    def to_representation(self, value):
        url = value.image.url
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # images = ProductImageField(
    #     queryset=ProductImage.objects.all(),
    #     many=True
    # )

    class Meta:
        model = Product
        fields = ('url', 'id', 'name', 'description',
                  'images')
