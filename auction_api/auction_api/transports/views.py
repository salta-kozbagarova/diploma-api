from .models import Transport
from .serializers import TransportSerializer
from rest_framework import viewsets

class TransportViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
