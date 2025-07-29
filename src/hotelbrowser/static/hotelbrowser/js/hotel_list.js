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

  // Show the list of cities that match the user's query.
  const showCityOptions = (cityOptions) => {
    const cityDataList = document.getElementById("city-options");

    const cityOptionElements = cityOptions.map(city => {
      const option = document.createElement("option");
      option.value = city.name;
      option.innerHTML = city.name;
      return option;
    });

    cityDataList.replaceChildren(...cityOptionElements);
  };

  // Get and display possible city names as the user types.
  const handleCityKeyUp = async (cityQuery) => {
    const response = await fetch("/api/cities/?" + new URLSearchParams({
      name: cityQuery
    }).toString());

    if (response.status === 200) {
      const cities = await response.json();
      showCityOptions(cities);
    } else {
      showHttpError(response.status);
    }
  };

  // When the city name text input's value changes, show all cities whose names
  // contain its new value.
  document.getElementById("city-name-text-input")
    .addEventListener("keyup", (event) => {
      const cityQuery = event.target.value;
      handleCityKeyUp(cityQuery);
    });
})();
