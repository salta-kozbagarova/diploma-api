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

class AdministrativeDivisionDetailSerializer(serializers.HyperlinkedModelSerializer):

    response = {}

    def to_representation(self, obj):
        self.get_hierarchy(obj)
        return self.response

    def get_hierarchy(self, obj):
        if obj.parent:
            new_resp = self.get_hierarchy(obj.parent)
            new_resp.update([('id', obj.pk), ('name', obj.name), ('parent_id', obj.parent_id), ('administrative_level_id', obj.administrative_level_id), ('subdivision',{})])
            return new_resp.get('subdivision')
        else:
            self.response.update([('id', obj.pk), ('name', obj.name), ('parent_id', obj.parent_id), ('administrative_level_id', obj.administrative_level_id), ('subdivision',{})])
            return self.response.get('subdivision')

    class Meta:
        model = AdministrativeDivision
        fields = ('url', 'id', 'name', 'parent', 'parent_id', 'administrative_level', 'administrative_level_id', 'subdivisions')
