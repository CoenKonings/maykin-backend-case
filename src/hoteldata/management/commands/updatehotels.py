import os

import requests
from django.core.management.base import BaseCommand
from dotenv import load_dotenv


class Command(BaseCommand):
    help = "Update hotel data"

    def handle(self, *args, **options):
        load_dotenv()
        username = os.environ["HOTELDATA_USERNAME"]
        password = os.environ["HOTELDATA_PASSWORD"]
        cities_url = os.environ["HOTELDATA_CITIES_URL"]
        hotels_url = os.environ["HOTELDATA_HOTELS_URL"]

        basic_auth = requests.auth.HTTPBasicAuth(username, password)

        self.stdout.write("Getting cities...")
        cities_result = requests.get(cities_url, auth=basic_auth)
        self.stdout.write(cities_result.text)

        self.stdout.write("Getting hotels...")
        hotels_result = requests.get(hotels_url, auth=basic_auth)
        self.stdout.write(hotels_result.text)
