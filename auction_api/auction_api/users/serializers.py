from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'is_staff', 'bargains_bargaintype_related')
