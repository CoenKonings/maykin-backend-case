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

  // Create a new element with the given tag and classes.
  const createElementWithClasses = (tag, classNames) => {
    const element = document.createElement(tag);
    classNames.forEach((className) => element.classList.add(className));
    return element;
  };

  // Create an element that displays a detail about the hotel.
  const createHotelDetailElement = (text) => {
    const hotelDetailElement = createElementWithClasses("div", ["hotel-detail"]);
    hotelDetailElement.appendChild(document.createTextNode(text));
    return hotelDetailElement;
  };

  // Create a visual separator.
  const createVerticalSeparatorElement = () => {
    const separator = createElementWithClasses("div", ["separator-vertical"]);
    separator.setAttribute("aria-hidden", "true");
    separator.setAttribute("role", "presentation");
  }

  // Show the hotels located in a city that matches the user's query.
  const showHotels = (citiesHotels) => {
    const hotelElements = citiesHotels.map(city => (
      city.hotel_set.map(hotel => {
        const hotelElement = createElementWithClasses("article", ["hotel-info"]);

        // Add h2 element with the hotel's name.
        const hotelTitleElement = createElementWithClasses("h2", ["hotel-name"]);
        hotelTitleElement.appendChild(document.createTextNode(hotel.name))
        hotelElement.appendChild(hotelTitleElement);

        // Add a div with the hotel's details (i.e. location and identifier).
        const hotelDetailsElement = createElementWithClasses("div", ["hotel-details"]);
        const hotelDetails = [
          `In: ${city.name}`,
          `ID: ${city.abbreviation + hotel.code}`,
        ];

        hotelDetails.forEach((detail, index) => {
          const hotelDetailElement = createHotelDetailElement(detail);
          hotelDetailsElement.appendChild(hotelDetailElement);

          if (index !== 0) {
            hotelDetailsElement.appendChild(createVerticalSeparatorElement());
          }
        });

        hotelElement.appendChild(hotelDetailsElement);

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
})();
