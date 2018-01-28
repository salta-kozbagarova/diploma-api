from .models import Painting
from .serializers import PaintingSerializer
from rest_framework import viewsets

class PaintingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
