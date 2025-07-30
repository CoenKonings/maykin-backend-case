from rest_framework import serializers

from .models import City, Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ["name", "code"]


class CitiesHotelsSerializer(serializers.ModelSerializer):
    hotel_set = HotelSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ["name", "abbreviation", "hotel_set"]
