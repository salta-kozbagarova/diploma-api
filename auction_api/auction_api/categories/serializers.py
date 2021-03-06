from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category
from rest_framework_recursive.fields import RecursiveField

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    parent = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),
        view_name='category-detail',
        lookup_field='code'
    )
    subcategories = RecursiveField(many=True)
    parent_code = serializers.ReadOnlyField(source="parent.code")

    class Meta:
        model = Category
        fields = ('url', 'id', 'code', 'name', 'image', 'parent', 'parent_id', 'subcategories', 'parent_code',
                  'created_by', 'updated_by', 'created_at', 'updated_at', 'is_active', 'is_deleted')
        lookup_field = 'code'
        extra_kwargs = {
            'url': {'lookup_field': 'code'}
        }
