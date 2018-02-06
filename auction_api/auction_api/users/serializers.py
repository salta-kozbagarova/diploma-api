from rest_framework import serializers
from .models import User, UserAddress, UserPhone
from auction_api.administrative_division.serializers import AdministrativeDivisionSerializer

class UserAddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserAddress
        fields = ('url', 'id', 'user', 'administrative_division')

class UserPhoneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserPhone
        fields = ('url', 'id', 'user', 'phone', 'is_main')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    addresses = AdministrativeDivisionSerializer(many=True)
    phonenumbers = UserPhoneSerializer(many=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'is_staff', 'password', 'addresses', 'phonenumbers')
        extra_kwargs = {'password': {'write_only': True}}
