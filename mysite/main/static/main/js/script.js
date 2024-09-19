// Get the popup element
const popup = document.getElementById("popup");

// Get the button that opens the popup
const openPopupBtn = document.getElementById("openPopup");

// Get the <span> element that closes the popup
const closePopupBtn = document.getElementById("closePopup");

// Open the popup when the user clicks the button
openPopupBtn.addEventListener("click", function () {
  popuep.style.display = "flex";
});

// Close the popup when the user clicks on <span> (x)
closePopupBtn.addEventListener("click", function () {
  popup.style.display = "none";
});

// Close the popup if the user clicks outside the popup content
window.addEventListener("click", function (event) {
  if (event.target === popup) {
    popup.style.display = "none";
  }
});
