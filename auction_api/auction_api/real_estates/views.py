from .models import Mansion
from .serializers import MansionSerializer
from rest_framework import viewsets

class MansionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Mansion.objects.all()
    serializer_class = MansionSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
