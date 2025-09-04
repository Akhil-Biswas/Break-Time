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

// detail

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

// Select all addTocart containers

const carts = document.querySelectorAll(".addTocart");

carts.forEach(cart => {

    const itemCard = cart.closest(".itemCard"); // find parent card

    const itemId = itemCard.getAttribute("item-id");



    const removeItem = cart.querySelector(".removeItem");

    const quantity = cart.querySelector(".quantity");

    const addItem = cart.querySelector(".addItem");

    //image

    const addimg = cart.querySelector("image.addItem");



    let totalQuantity = 0;

    function updateQuantity() {

        quantity.textContent = totalQuantity;

        console.log(itemId, totalQuantity);

        // send to server

        sendCartData(itemId, totalQuantity);

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