from .models import AdministrativeLevel, AdministrativeDivision
from .serializers import AdministrativeDivisionSerializer, AdministrativeLevelSerializer
from rest_framework import viewsets

class AdministrativeLevelViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = AdministrativeLevel.objects.all()
    serializer_class = AdministrativeLevelSerializer

class AdministrativeDivisionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = AdministrativeDivision.objects.all()
    serializer_class = AdministrativeDivisionSerializer
