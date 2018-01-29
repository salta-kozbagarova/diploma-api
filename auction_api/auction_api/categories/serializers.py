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

    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'image', 'parent', 'subcategories', 'created_by', 'updated_by', 'created_at',
                  'updated_at', 'is_active', 'is_deleted')
        lookup_field = 'code'
        extra_kwargs = {
            'url': {'lookup_field': 'code'}
        }
