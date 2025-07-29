from django_filters import rest_framework as filters


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CityFilter(filters.FilterSet):
    """
    Filters cities by name.
    """

    name = filters.CharFilter(lookup_expr="icontains")


class HotelFilter(filters.FilterSet):
    """
    Filters hotels by city abbreviation.
    """

    city__abbreviation = CharInFilter(lookup_expr="in")
