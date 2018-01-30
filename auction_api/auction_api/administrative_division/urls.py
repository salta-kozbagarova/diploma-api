from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'adm-divisions', views.AdministrativeDivisionViewSet)
router.register(r'adm-levels', views.AdministrativeLevelViewSet)

adm_division_detail = views.AdministrativeDivisionDetailViewSet.as_view({
    'get': 'retrieve'
})

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^adm-divisions-detail/(?P<pk>[0-9]+)/$', adm_division_detail, name='adm-division-detail'),
]
