from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'bargains', views.BargainViewSet)
router.register(r'bargain-types', views.BargainTypeViewSet)
router.register(r'bargain-bets', views.BargainBetViewSet)
router.register(r'bargain-comments', views.BargainCommentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
]
