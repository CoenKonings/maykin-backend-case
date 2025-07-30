from django_filters.views import FilterView

from hoteldata.models import Hotel

from .filters import HotelFilter


class HotelListView(FilterView):
    """
    A view that allows user to filter a list of hotels by city.
    """

    template_name = "hotelbrowser/hotel_list.html"
    context_object_name = "hotel_list"
    filterset_class = HotelFilter

    def get_queryset(self):
        """
        Return a queryset of all hotels ordered alphabetically by city name and
        hotel name.
        """
        return Hotel.objects.order_by("city__name", "name")
