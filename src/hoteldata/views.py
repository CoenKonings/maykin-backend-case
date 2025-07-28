from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import City, Hotel


class HotelListView(ListView):
    model = Hotel


class CityHotelListView(ListView):
    template_name = "hoteldata/hotel_list.html"

    def get_queryset(self):
        self.city = get_object_or_404(City, abbreviation=self.kwargs["city"])
        return Hotel.objects.filter(city=self.city)
