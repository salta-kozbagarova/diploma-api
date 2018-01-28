from .models import Headphone
from .serializers import HeadphoneSerializer
from rest_framework import viewsets

class HeadphoneViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Headphone.objects.all()
    serializer_class = HeadphoneSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
