from rest_framework import serializers
from .models import Bargain, BargainType

class BargainSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bargain
        fields = ('url', 'id', 'end_date', 'bargain_type',
                  'start_price', 'current_price', 'name', 'image',)

class BargainTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BargainType
        fields = ('url', 'id', 'name', 'created_by', 'updated_by')
        depth = 2
