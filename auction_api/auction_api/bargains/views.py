from .models import Bargain, BargainType, BargainBet, BargainComment
from .serializers import BargainSerializer, BargainTypeSerializer, BargainBetSerializer, BargainCommentSerializer
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from .filters import BargainFilter
from django.db.models import Q
from rest_framework.response import Response
# Create your views here.

class BargainViewSet(viewsets.ModelViewSet):

    queryset = Bargain.objects.all()
    serializer_class = BargainSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_class = BargainFilter

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        q = self.request.query_params.get('q', None)
        header_and_description = self.request.query_params.get('header_and_description', None)
        if q is not None:
            if header_and_description is not None and header_and_description == 'true':
                self.queryset = self.queryset.filter(Q(product__name__icontains=q) | Q(product__description__icontains=q))
            else:
                self.queryset = self.queryset.filter(product__name__icontains=q)
        only_with_image = self.request.query_params.get('only_with_image', None)
        if only_with_image == 'true':
            self.queryset = self.queryset.filter(product__images__isnull=False).distinct()
                # .exclude(product__images='')
        return self.queryset

    def list(self, request, *args, **kwargs):
        only_quantity = request.query_params.get('only_quantity', None)
        if only_quantity is not None and only_quantity == 'true':
            queryset = self.filter_queryset(self.get_queryset())
            count = queryset.count()
            return Response(count)
        else:
            return super(BargainViewSet, self).list(request, *args, **kwargs)

class BargainTypeViewSet(viewsets.ModelViewSet):

    queryset = BargainType.objects.all()
    serializer_class = BargainTypeSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class BargainBetViewSet(viewsets.ModelViewSet):

    queryset = BargainBet.objects.all()
    serializer_class = BargainBetSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class BargainCommentViewSet(viewsets.ModelViewSet):

    queryset = BargainComment.objects.all()
    serializer_class = BargainCommentSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
