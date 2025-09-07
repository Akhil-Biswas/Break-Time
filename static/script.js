// Select all addTocart containers
const carts = document.querySelectorAll(".addTocart");

carts.forEach(cart => {
    const itemCard = cart.closest(".itemCard"); // find parent card

    const itemId = itemCard.getAttribute("item-id");
    const removeItem = cart.querySelector(".removeItem");
    const quantity = cart.querySelector(".quantity");
    const addItem = cart.querySelector(".addItem");

    let totalQuantity = 0;
    function updateQuantity() {
        quantity.textContent = totalQuantity;
        console.log(itemId, totalQuantity);
        // send to server

        if (totalQuantity === 0) {
            removeItem.style.display = "none";
            quantity.style.display = "none";
        } else {
            removeItem.style.display = "inline-block";
            quantity.style.display = "inline-block";
        }
    }
    // Add button
    addItem.addEventListener("click", () => {
        totalQuantity++;
        updateQuantity();
    });
    // Remove button
    removeItem.addEventListener("click", () => {
        if (totalQuantity > 0) {
            totalQuantity--;
            updateQuantity();
        }
    });
    quantity.addEventListener("click", () => {
        if (totalQuantity > 0) {
            totalQuantity++;
            updateQuantity();
        }
    });
    // Initialize
    updateQuantity();
});