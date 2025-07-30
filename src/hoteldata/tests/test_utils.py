from django.test import TestCase

from ..models import City, Hotel
from ..utils import list_to_city, list_to_hotel


class TestImportUtils(TestCase):
    @classmethod
    def setUp(cls):
        City.objects.create(
            name="Amsterdam",
            abbreviation="AMS",
        )

    def test_list_to_city(self):
        list_to_city(["DHG", "Den Haag"])
        city = City.objects.get(abbreviation="DHG")
        # Check if the city is correctly created.
        self.assertEqual(city.name, "Den Haag")

        list_to_city(["AMS", "Amstelveen"])
        city = City.objects.get(abbreviation="AMS")
        # Check if the city's name was changed correctly.
        self.assertEqual(city.name, "Amstelveen")

        num_cities = City.objects.count()
        list_to_city(["AAAA", "Kan niet"])
        # Check if city with abbreviation AAAA was not created.
        self.assertEqual(num_cities, City.objects.count())

    def test_list_to_hotel(self):
        list_to_hotel(["AMS", "AMS00", "Hotel 1"])
        list_to_hotel(["EEE", "EEE00", "Hotel 2"])
        amsterdam = City.objects.get(pk=1)

        try:
            hotel_1 = Hotel.objects.get(city=amsterdam, code="00")
        except Hotel.DoesNotExist:
            hotel_1 = Hotel.objects.create(city=amsterdam, code="00", name="Hotel 1")
            self.fail("List_to_hotel did not create a hotel.")

        # Check if no hotel was created in a non-existent city.
        self.assertEqual(Hotel.objects.count(), 1)
        # Check if the created hotel has the correct city.
        self.assertEqual(hotel_1.city, amsterdam)
        # Check if the created hotel has the expected name.
        self.assertEqual(hotel_1.name, "Hotel 1")
        # Check if the created hotel has the correct code.
        self.assertEqual(hotel_1.code, "00")
