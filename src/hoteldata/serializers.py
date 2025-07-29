from rest_framework import serializers

from .models import City, Hotel


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.SlugRelatedField(many=False, read_only=True, slug_field="name")

    class Meta:
        model = Hotel
        fields = ["name", "city"]


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ["name", "abbreviation"]
