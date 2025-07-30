# Overview
The Django project is called _hotelmgmt_, and can be found in `/src`. The project consists of two apps: [_hoteldata_](apps/hoteldata.md) and [_hotelbrowser_](apps/hotelbrowser.md). Hoteldata manages the available information about hotels: it provides a [management command](commands.md) to update information about hotels and/or cities, and implements a [RESTful API](endpoints.md) to retrieve data. Hotelbrowser implements a front-end that can be used to view hotels and filter them by city.

While working with the data, I made several assumptions. These are documented in [[assumptions]].
