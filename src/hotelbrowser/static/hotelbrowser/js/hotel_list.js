(() => { // Don't pollute global namespace.

  // Show elements that require JS to be enabled.
  Array.prototype.map.call(
    document.getElementsByClassName("js-only"),
    element => element.classList.toggle("js-only")
  );

  // Show an HTTP error encountered while fetching data.
  const showHttpError = (statusCode) => {
    const errorMessage = "Something went wrong. Status code: " + statusCode;
    document.getElementById("error").innerText = errorMessage;
  };

  // Show the hotels located in a city that matches the user's query.
  const showHotels = (citiesHotels) => {
    const hotelElements = citiesHotels.map(city => (
      city.hotel_set.map(hotelName => {
        const hotelElement = document.createElement("article");
        hotelElement.classList.add("hotel-info");

        const hotelTitleElement = document.createElement("h2");
        hotelTitleElement.classList.add("hotel-name");
        hotelTitleElement.appendChild(document.createTextNode(hotelName))
        hotelElement.appendChild(hotelTitleElement);

        const hotelLocationElement = document.createElement("div");
        hotelLocationElement.classList.add("hotel-location");
        hotelLocationElement.appendChild(document.createTextNode(city.name));
        hotelElement.appendChild(hotelLocationElement);

        return hotelElement;
      })
    )).flat();

    const hotelListElement = document.getElementById("hotel-list");

    if (hotelElements.length !== 0) {
      hotelListElement.replaceChildren(...hotelElements);
    } else {
      const listEmptyElement = document.createElement("span");
      listEmptyElement.classList.add("italics");
      listEmptyElement.appendChild(document.createTextNode("No hotels found"));
      hotelListElement.replaceChildren(listEmptyElement);
    }
  };

  // Show the list of cities that match the user's query.
  const showCityOptions = (cities) => {
    const cityOptionElements = cities.map(city => {
      const option = document.createElement("option");
      option.value = city.name;
      option.innerHTML = city.name;
      return option;
    });

    const cityDataList = document.getElementById("city-options");
    cityDataList.replaceChildren(...cityOptionElements);
  };

  // Get and display possible city names and hotels as the user types.
  const getCitiesHotels = async (cityQuery) => {
    const response = await fetch("/api/cities-hotels/?" + new URLSearchParams({
      name: cityQuery
    }).toString());

    if (response.status === 200) {
      const citiesHotels = await response.json();
      showCityOptions(citiesHotels);
      showHotels(citiesHotels);
    } else {
      showHttpError(response.status);
    }
  };

  // When the city name text input's value changes, show all cities whose names
  // contain its new value.
  document.getElementById("city-name-text-input")
    .addEventListener("keyup", (event) => {
      const cityQuery = event.target.value;
      getCitiesHotels(cityQuery);
    });

  // Get city and hotel data when page loads.
  getCitiesHotels("");
})();
