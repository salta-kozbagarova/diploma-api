from .models import Category
from .serializers import CategorySerializer
from rest_framework import viewsets
from .filters import CategoryFilter
from .permissions import IsAdminOrReadOnly
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'code'
    permission_classes = (IsAdminOrReadOnly,)
    filter_class = CategoryFilter

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
