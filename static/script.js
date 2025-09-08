function saveCartData(itemId, quantity) {
    // Get existing cart or initialize empty
    let cart = JSON.parse(localStorage.getItem("Cart")) || {};

    // If quantity <= 0, remove the item
    if (quantity <= 0) {
        delete cart[itemId];
    } else {
        // Otherwise add/update the item
        cart[itemId] = quantity;
    }

    // Save updated cart back to localStorage
    localStorage.setItem("Cart", JSON.stringify(cart));

    console.info("Cart saved:");
    console.table(cart);
}

// Select all addTocart containers
const carts = document.querySelectorAll(".addTocart");

carts.forEach(cart => {
    const itemCard = cart.closest(".itemCard"); // find parent card

    const itemId = itemCard.getAttribute("item-id");
    const removeItem = cart.querySelector(".removeItem");
    const quantity = cart.querySelector(".quantity");
    const addItem = cart.querySelector(".addItem");

    let cartData = JSON.parse(localStorage.getItem("Cart")) || {};
    let totalQuantity = cartData[itemId] || 0;    //first check in localstorage if not then quantity is 0

    function updateQuantity() {
        quantity.textContent = totalQuantity;
        console.log(itemId, totalQuantity);
        // store in localstorage
        saveCartData(itemId, totalQuantity);
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
    
    // Initialize
    updateQuantity();
});