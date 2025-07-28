import csv
import os
from io import StringIO

import requests
from dotenv import load_dotenv

from .models import City


def get_request_ok(username, password, url):
    """
    Send an authenticated GET request to the given URL. Return the response's
    text if the status code is 200, raise an exception otherwise.

    @param username:    The username used to authenticate the HTTP request to
                        the URL.
    @param password:    The password used to authenticate the HTTP request to
                        the URL.
    @param url:         The URL of the CSV file that contains the data to be
                        imported.

    @returns:   The response if the status code is 200.
    """
    response = requests.get(url, auth=(username, password))

    if response.status_code != 200:
        raise RuntimeError(f"Request returned status code {response.status_code}")

    return response.text


def list_to_city(city_data):
    """
    Given a list containing a three letter abbreviation and the name of a city,
    update the database. If a city with the given abbreviation exists, update
    its name if it has changed. If no such city exists, add it to the database.

    @param city_data:   A list containing a city's three letter abbreviation
                        and name as its first two elements.
    """
    abbreviation = city_data[0]
    name = city_data[1]

    try:
        city = City.objects.get(abbreviation=abbreviation)

        if city.name != name:
            city.name = name
            city.save()

    except City.DoesNotExist:
        city = City(abbreviation=abbreviation, name=name)
        city.save()


def list_to_hotel(hotel_data):
    """
    Given a list containing a three letter abbreviation of a city, a hotel code
    and a hotel's name, update the database. If a hotel with the given code
    exists, update it if necessary. Otherwise, add a new hotel to the database.
    If no city with the given abbreviation exists, set it to null.

    @param hotel_data:  A list containing a city's three letter abbreviation,
                        and a hotel's code and name as its first three
                        elements.
    """

    # TODO
    pass


def import_csv_data(username, password, url, row_import_callback):
    """
    Import city data from the given url to the database.

    @param username:            The username used to authenticate the HTTP
                                request to the URL.
    @param password:            The password used to authenticate the HTTP
                                request to the URL.
    @param url:                 The URL of the CSV file that contains the data
                                to be imported.
    @param row_import_callback: A function that takes a row of CSV data and
                                uses it to update the database.
    """
    response_text = get_request_ok(username, password, url)
    response_file = StringIO(response_text)
    csv_reader = csv.reader(response_file, delimiter=";")

    for row in csv_reader:
        row_import_callback(row)


def import_hotels_cities():
    """
    Import city and hotel data from the CSV files found at the URLs in the .env
    to the database.
    """
    load_dotenv()
    username = os.environ["HOTELDATA_USERNAME"]
    password = os.environ["HOTELDATA_PASSWORD"]
    cities_url = os.environ["HOTELDATA_CITIES_URL"]

    import_csv_data(username, password, cities_url, list_to_city)
