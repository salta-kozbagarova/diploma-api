from .models import Language
from .serializers import LanguageSerializer
from rest_framework import viewsets

class LanguageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
