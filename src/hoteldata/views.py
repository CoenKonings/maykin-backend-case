from django.views.generic import ListView

from .models import Hotel


class HotelListView(ListView):
    model = Hotel
