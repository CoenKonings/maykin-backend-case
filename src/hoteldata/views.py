from django_filters import rest_framework as filters
from rest_framework import viewsets

from .filters import HotelFilter
from .models import Hotel
from .serializers import HotelBrowserSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelBrowserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HotelFilter
