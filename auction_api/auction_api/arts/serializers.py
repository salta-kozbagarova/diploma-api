from rest_framework import serializers
from .models import Painting

class PaintingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Painting
        fields = '__all__'
