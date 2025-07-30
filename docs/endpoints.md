# API Endpoints
The following endpoints are available:
- `/api/cities-hotels/`: Retrieve a list of all cities and the hotels located in each city. Optionally, GET parameter `name` can be set to retrieve only the cities whose name contains the value of said parameter.\
*Example*: sending a GET request to `api/cities-hotels/?name=mst` results in\
```json
[
    {
        "name": "Amsterdam",
        "abbreviation": "AMS",
        "hotel_set": [
            {
                "name": "Ibis Amsterdam Airport",
                "code": "01"
            },
            {
                "name": "Novotel Amsterdam Airport",
                "code": "02"
            }
        ]
    }
]
```
