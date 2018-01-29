from .models import AdBanner
from .serializers import AdBannerSerializer
from rest_framework import viewsets
# Create your views here.

class AdBannerViewSet(viewsets.ModelViewSet):

    queryset = AdBanner.objects.all()
    serializer_class = AdBannerSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
