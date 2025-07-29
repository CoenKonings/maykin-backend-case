from django.urls import include, path
from rest_framework import routers

from .views import HotelViewSet

router = routers.DefaultRouter()
router.register(r"hotels", HotelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
