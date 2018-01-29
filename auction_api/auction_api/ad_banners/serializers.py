from rest_framework import serializers
from .models import AdBanner

class AdBannerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AdBanner
        fields = ('url', 'id', 'name', 'image',
                  'created_by', 'updated_by', 'created_at', 'updated_at', 'is_active', 'is_deleted')
