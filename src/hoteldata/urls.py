from django.urls import include, path
from rest_framework import routers

from .views import CitiesHotelsViewSet

router = routers.DefaultRouter()
router.register(r"cities-hotels", CitiesHotelsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
