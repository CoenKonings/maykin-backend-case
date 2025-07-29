from rest_framework import viewsets

from .models import Hotel
from .serializers import HotelBrowserSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelBrowserSerializer
