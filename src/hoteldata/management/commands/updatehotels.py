from django.core.management.base import BaseCommand

from hoteldata.utils import import_hotels_cities


class Command(BaseCommand):
    help = "Update hotel data"

    def handle(self, *args, **options):
        """
        Using the credentials and URLs from the .env, import data about hotels
        and cities. Add to or update the database accordingly.
        """
        self.stdout.write("Importing hotels and cities...")
        import_hotels_cities(stdout=self.stdout)
        self.stdout.write(self.style.SUCCESS("Successfully imported data."))
