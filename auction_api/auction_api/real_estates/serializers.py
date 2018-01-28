from rest_framework import serializers
from .models import Mansion

class MansionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Mansion
        fields = '__all__'
