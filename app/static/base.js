//++++++++++++++++++++++++++++++++++++++++++++++++++++++
// DETAIL MENU
//++++++++++++++++++++++++++++++++++++++++++++++++++++++
// Select elements
const detailMenu = document.querySelector(".Detail");
const detailOpen = document.querySelector("#detailOpen");
const detailClose = document.querySelector("#detailClose");
// Open menu
detailOpen.addEventListener("click", () => {
    detailMenu.style.display = "block"; // show menu
});

// Close menu
detailClose.addEventListener("click", () => {
    detailMenu.style.display = "none"; // hide menu
});