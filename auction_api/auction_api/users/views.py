from .models import User, UserAddress, UserPhone
from .serializers import UserSerializer, UserAddressSerializer, UserPhoneSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAddressViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

class UserPhoneViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = UserPhone.objects.all()
    serializer_class = UserPhoneSerializer
