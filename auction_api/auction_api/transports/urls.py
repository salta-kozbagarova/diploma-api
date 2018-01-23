from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cars', views.CarViewSet)
router.register(r'car-makes', views.CarMakeViewSet)
router.register(r'car-models', views.CarModelViewSet)
router.register(r'car-bodies', views.CarBodyViewSet)
router.register(r'transmissions', views.TransmissionViewSet)
router.register(r'transport-images', views.TransportImageViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
]
