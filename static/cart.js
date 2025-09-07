// Select all addToCart containers
const carts = document.querySelectorAll(".addTocart");

carts.forEach(cart => {
    const itemCard = cart.closest(".item"); // find parent card
    const itemId = itemCard.getAttribute("item-id");

    const removeItem = cart.querySelector(".removeItem");
    const quantity = cart.querySelector(".quantity");
    const addItem = cart.querySelector(".addItem");
    const delItem = itemCard.querySelector(".delItem");

    let totalQuantity = 1;

    function updateQuantity() {
        quantity.textContent = totalQuantity;

        console.log(itemId, totalQuantity);
        // store in localstorage

        // send to server

        if (totalQuantity === 0) {
            console.warn("item removed from cart")
            itemCard.remove()
        } else {
            removeItem.style.display = "inline-block";
            quantity.style.display = "inline-block";
        }
    }

    // Add button
    addItem.addEventListener("click", () => {
        console.info("clicked on Add");
        totalQuantity++;
        updateQuantity();
    });

    // Remove button
    removeItem.addEventListener("click", () => {
        console.info("clicked on Remove");
        if (totalQuantity > 0) {
            totalQuantity--;
            updateQuantity();
        }
    });

    // Delete button
    delItem.addEventListener("click", () => {
        console.info("clicked on delItem");
        totalQuantity = 0;
        updateQuantity();
    });

    // Initialize
    updateQuantity();
});