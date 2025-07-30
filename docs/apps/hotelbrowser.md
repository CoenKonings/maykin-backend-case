# Hotelbrowser
The _hotelbrowser_ app implements a front-end in which users can view and filter the available hotels in the [API](../endpoints.md) implemented by the [hoteldata](hoteldata.md) app. To do so, it uses the [Django Rest Framework](https://www.django-rest-framework.org/) and [Django-filter](https://pypi.org/project/django-filter/) libraries.

## Models
This app implements no models.

## Views
- `HotelListView`: A [`FilterView`](https://django-filter.readthedocs.io/en/stable/guide/usage.html#generic-view-configuration) that allows users to filter the listed hotels.

## Templates
- `hotelbrowser/base.html`: Contains the HTML head and a navbar.
- `hotelbrowser/hotel_list.html`: Shows the filter section and the hotel list. Uses the `filter` form supplied by `HotelListView` for users with JavaScript disabled. Users with JavaScript enabled can use a text input to asynchronously get hotels in cities that match their query.
