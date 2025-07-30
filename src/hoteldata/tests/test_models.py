from django.test import TestCase

from ..models import City, Hotel


class TestCity(TestCase):
    @classmethod
    def setUp(cls):
        City.objects.create(
            name="Amsterdam",
            abbreviation="AMS",
        )

        City.objects.create(
            name="Den Haag",
            abbreviation="DHG",
        )

        Hotel.objects.create(
            name="The Collector",
            code="00",
            city=City.objects.get(pk=2),
        )

        Hotel.objects.create(
            name="The Manor Amsterdam",
            code="00",
            city=City.objects.get(pk=1),
        )

        Hotel.objects.create(
            name="Nog Een Hotel",
            code="01",
            city=City.objects.get(pk=1),
        )

    def test_city_str(self):
        """Test if string representation is working properly."""
        amsterdam = City.objects.get(pk=1)
        den_haag = City.objects.get(pk=2)
        self.assertEqual(str(amsterdam), "Amsterdam (AMS)")
        self.assertEqual(str(den_haag), "Den Haag (DHG)")

    def test_get_num_hotels(self):
        """Test if the number of hotels is correctly found."""
        amsterdam = City.objects.get(pk=1)
        den_haag = City.objects.get(pk=2)
        self.assertEqual(amsterdam.get_num_hotels(), 2)
        self.assertEqual(den_haag.get_num_hotels(), 1)
