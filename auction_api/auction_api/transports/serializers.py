from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Transport

class TransportSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Transport
        fields = ('url', 'id', 'name', 'description', 'products_productimage_related')
