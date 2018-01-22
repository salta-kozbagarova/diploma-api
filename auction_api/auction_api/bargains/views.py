from .models import Bargain, BargainType
from .serializers import BargainSerializer, BargainTypeSerializer
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
# Create your views here.

class BargainViewSet(viewsets.ModelViewSet):

    queryset = Bargain.objects.all()
    serializer_class = BargainSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class BargainTypeViewSet(viewsets.ModelViewSet):

    queryset = BargainType.objects.all()
    serializer_class = BargainTypeSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
