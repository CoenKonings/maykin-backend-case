# Assumptions
Here, I documented the assumptions I made. Normally, I'd check these with the client.
- The codes in the hotel CSV, that consist of the city's three letter abbreviation and a two character postfix, are assumed to be the hotels' unique identifiers. They are referred to as the hotel's identifier in both the code and the documentation.
- Duplicate hotel names with different identifiers[^1] are assumed to be different locations of the same hotel. To differentiate them, the front-end implemented in [hotelbrowser](apps/hotelbrowser.md) displays the hotel's identifier as well.
- The letter code / identifier for a city is assumed to be at most three characters long.

[^1]: E.G. in Antwerp: Astioria (ANT04), Astoria (ANT78) and Astoria (ANT97).
