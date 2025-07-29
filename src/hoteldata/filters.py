from django_filters import rest_framework as filters


class HotelFilter(filters.FilterSet):
    city__name = filters.CharFilter(lookup_expr="icontains")
