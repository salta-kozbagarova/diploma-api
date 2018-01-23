from rest_framework import serializers
from .models import User, UserAddress, UserPhone

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'is_staff', 'password', 'bargains_bargaintype_related')

class UserAddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserAddress
        fields = ('url', 'id', 'user', 'administrative_division')
        depth = 2

class UserPhoneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserAddress
        fields = ('url', 'id', 'user', 'phone', 'is_main')
        depth = 2
