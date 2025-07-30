from rest_framework import serializers

from .models import City


class CitiesHotelsSerializer(serializers.HyperlinkedModelSerializer):
    hotel_set = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name", allow_null=True
    )

    class Meta:
        model = City
        fields = ["name", "hotel_set"]
