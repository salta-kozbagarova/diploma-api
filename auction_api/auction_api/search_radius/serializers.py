from rest_framework import serializers
from .models import SearchRadius

class SearchRadiusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SearchRadius
        fields = ('url', 'id', 'radius', 'metric')
