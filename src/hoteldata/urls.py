from django.urls import include, path
from rest_framework import routers

from .views import CityViewSet, HotelViewSet

router = routers.DefaultRouter()
router.register(r"hotels", HotelViewSet)
router.register(r"cities", CityViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
