from .models import SearchRadius
from .serializers import SearchRadiusSerializer
from rest_framework import viewsets

class SearchRadiusViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = SearchRadius.objects.all()
    serializer_class = SearchRadiusSerializer
