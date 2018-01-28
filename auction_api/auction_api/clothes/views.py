from .models import Jeans
from .serializers import JeansSerializer
from rest_framework import viewsets

class JeansViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Jeans.objects.all()
    serializer_class = JeansSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
