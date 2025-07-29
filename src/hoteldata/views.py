from django_filters import rest_framework as filters
from rest_framework import viewsets

from .filters import CityNameFilter
from .models import City
from .serializers import CitiesHotelsSerializer


class CitiesHotelsViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitiesHotelsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CityNameFilter
