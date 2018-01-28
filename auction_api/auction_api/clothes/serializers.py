from rest_framework import serializers
from .models import Jeans

class JeansSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Jeans
        fields = '__all__'
