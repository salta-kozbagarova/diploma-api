from rest_framework import serializers
from .models import Headphone

class HeadphoneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Headphone
        fields = '__all__'
