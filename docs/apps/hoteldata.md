# Hoteldata
The _hoteldata_ app implements an [API](../endpoints.md) using [Django Rest Framework](https://www.django-rest-framework.org/) and [Django-filter](https://pypi.org/project/django-filter/).

## Models
- `City`: Represents a city. Each city has a `name` and a three letter `abbreviation`. The `Hotel`s located in each city can by found in the `hotel_set` property.
- `Hotel`: Represents a hotel. Each hotel has a name and is located in a city. The three letter `abbreviation` of a `Hotel`'s `city`, followed by the `Hotel`'s `code` creates the `Hotel`'s identifier.

## Views
- `CitiesHotelsViewSet`: A Django Rest Framework ModelViewSet that manages the logic for the `/api/cities-hotels/` endpoint.

## Templates
This app has no templates.

## Endpoints
Refer to the [endpoints documentation](../endpoints.md) for more detailed descriptions.
- `/api/cities-hotels/`: Find cities and the associated hotels.
