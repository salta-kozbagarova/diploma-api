from rest_framework import serializers
from .models import AdministrativeLevel, AdministrativeDivision

class AdministrativeLevelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AdministrativeLevel
        fields = ('url', 'id', 'name')

class AdministrativeDivisionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AdministrativeDivision
        fields = ('url', 'id', 'name', 'parent', 'administrative_level')
