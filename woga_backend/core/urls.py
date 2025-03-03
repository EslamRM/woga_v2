from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupportViewSet,ContactViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register("contact", ContactViewSet, basename="Contact")
router.register("support", SupportViewSet, basename="Support")


urlpatterns = [
    path("", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
