(() => { // Don't pollute global namespace.

  // Show elements that require JS to be enabled.
  Array.prototype.map.call(
    document.getElementsByClassName("js-only"),
    element => element.classList.toggle("js-only")
  );

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

  // Get all cities whose names contain the given query and display them as
  // options.
  const handleCityQuery = async (cityQuery) => {
    const response = await fetch("/api/cities/?" + new URLSearchParams({
      name: cityQuery
    }).toString());

    if (response.status === 200) {
      const cities = await response.json();
      showCityOptions(cities);
    } else {
      showError(response.status);
    }
  };

  // When the city name text input's value changes, show all cities whose names
  // contain its new value.
  document.getElementById("city-name-text-input")
    .addEventListener("keyup", (event) => {
      const cityQuery = event.target.value;
      handleCityQuery(cityQuery);
    });
})();
