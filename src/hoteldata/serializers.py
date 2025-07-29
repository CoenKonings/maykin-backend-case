from rest_framework import serializers

from .models import Hotel


class HotelBrowserSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.SlugRelatedField(many=False, read_only=True, slug_field="name")

    class Meta:
        model = Hotel
        fields = ["name", "city"]
