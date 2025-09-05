// store in localstorage
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

    console.log("Cart saved:", cart);
}

/*
//sand data to server

function sendCartData(itemId, quantity) {
    fetch("/update_cart", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            itemid: itemId,
            quantity: quantity
        })
    })
    //.then(response => response.json())

    //.then(data => {

    // console.log("Cart updated:", data);

    // })

    //.catch(error => console.error("Error:", error));
}

*/

// Select all addToCart containers
let sevedItem= localStorage.getItem("Cart") || {};

const carts = document.querySelectorAll(".addTocart");

carts.forEach(cart => {
    const itemCard = cart.closest(".item"); // find parent card
    const itemId = itemCard.getAttribute("item-id");

    const removeItem = cart.querySelector(".removeItem");
    const quantity = cart.querySelector(".quantity");
    const addItem = cart.querySelector(".addItem");
    const delItem = itemCard.querySelector(".delItem");

    let totalQuantity = JSON.parse(localStorage.getItem("Cart"))
[itemId] ||0 ;   //first check in localstorage if not then quantity is 0

    function updateQuantity() {
        quantity.textContent = totalQuantity;

        console.log(itemId, totalQuantity);
        // store in localstorage
        saveCartData(itemId, totalQuantity);
        // send to server
        //sendCartData(itemId, totalQuantity);

        if (totalQuantity === 0) {
            itemCard.remove()
            //removeItem.style.display = "none";
            //quantity.style.display = "none";
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

    // Click on quantity to increase
    quantity.addEventListener("click", () => {
        if (totalQuantity > 0) {
            totalQuantity++;
            updateQuantity();
        }
    });

    // Delete button
    delItem.addEventListener("click", () => {
        totalQuantity = 0;
        updateQuantity();
    });

    // Initialize
    updateQuantity();
});