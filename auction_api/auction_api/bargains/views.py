from .models import Bargain, BargainType, BargainBet, BargainComment, BargainAddress
from .serializers import BargainSerializer, BargainTypeSerializer, BargainBetSerializer, BargainCommentSerializer, BargainAddressSerializer
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

class BargainBetViewSet(viewsets.ModelViewSet):

    queryset = BargainBet.objects.all()
    serializer_class = BargainBetSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class BargainCommentViewSet(viewsets.ModelViewSet):

    queryset = BargainComment.objects.all()
    serializer_class = BargainCommentSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class BargainAddressViewSet(viewsets.ModelViewSet):

    queryset = BargainAddress.objects.all()
    serializer_class = BargainAddressSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
