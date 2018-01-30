from rest_framework import serializers
from .models import AdministrativeLevel, AdministrativeDivision
from rest_framework_recursive.fields import RecursiveField

class AdministrativeLevelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AdministrativeLevel
        fields = ('url', 'id', 'name')

class AdministrativeDivisionSerializer(serializers.HyperlinkedModelSerializer):
    subdivisions = RecursiveField(many=True)

    class Meta:
        model = AdministrativeDivision
        fields = ('url', 'id', 'name', 'parent', 'parent_id', 'administrative_level', 'administrative_level_id', 'subdivisions')
