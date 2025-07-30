import django_filters


class HotelFilter(django_filters.FilterSet):
    """
    Filter hotels by city name.
    """

    city__name = django_filters.CharFilter(lookup_expr="icontains", label="City")
