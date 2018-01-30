from .models import AdministrativeLevel, AdministrativeDivision
from .serializers import AdministrativeDivisionSerializer, AdministrativeLevelSerializer, AdministrativeDivisionDetailSerializer
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

class AdministrativeDivisionDetailViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = AdministrativeDivision.objects.all()
    serializer_class = AdministrativeDivisionDetailSerializer
