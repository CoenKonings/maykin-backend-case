(() => { // Don't pollute global namespace.

  // Show elements that require JS.
  Array.prototype.map.call(
    document.getElementsByClassName("js-only"),
    element => element.classList.toggle("js-only")
  );

})();
