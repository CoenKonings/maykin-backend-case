from django_filters import rest_framework as filters


class CityNameFilter(filters.FilterSet):
    """
    Filters cities by name.
    """

    name = filters.CharFilter(lookup_expr="icontains")
