function saveCartData(itemId,itemname,itemPrice,quantity,itemType,itemPic) {
    // Get existing cart or initialize empty
    let cart = JSON.parse(localStorage.getItem("Cart")) || {};

    // If quantity <= 0, remove the item
    if (quantity <= 0) {
        delete cart[itemId];
    } else {
        // Otherwise add/update the item
        cart[itemId] = {
            "itemName":itemname,
            "itemPrice":itemPrice,
            "quantity":quantity,
            "itemType":itemType,
            "itemPic":itemPic
        };
    }

    // Save updated cart back to localStorage
    localStorage.setItem("Cart", JSON.stringify(cart));

    console.log("Cart saved:", cart);
}
/*
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

// Detail menu
const detailMenu = document.querySelector(".Detail");
const detailOpen = document.querySelector("#detailOpen");
const detailClose = document.querySelector("#detailClose");

// Open menu
detailOpen.addEventListener("click", () => {
    detailMenu.style.display = "block";
});

// Close menu
detailClose.addEventListener("click", () => {
    detailMenu.style.display = "none";
});

// Select all addToCart containers
const carts = document.querySelectorAll(".addTocart");

carts.forEach(cart => {
    const itemCard = cart.closest(".itemCard"); // find parent card
    const itemId = itemCard.getAttribute("item-id");
    const itemName = itemCard.querySelector(".itemName").textContent.trim();
    const itemPrice = itemCard.querySelector(".itemPrice").textContent.replace('₹','').trim();
        //url: static/src/itemType.svg
    const itemType = itemCard.getAttribute("item_type");
    const itemPic =itemCard.querySelector(".itemPic").src;
    const removeItem = cart.querySelector(".removeItem");
    const quantity = cart.querySelector(".quantity");
    const addItem = cart.querySelector(".addItem");

    const cartData = JSON.parse(localStorage.getItem("Cart")) || {};
    let totalQuantity = cartData[itemId] ? cartData[itemId].quantity : 0;   //first check in localstorage if not then quantity is 0


    function updateQuantity() {
        quantity.textContent = totalQuantity;

        console.log(itemId, totalQuantity);

        // store in localstorage
        saveCartData(itemId,itemName,itemPrice,totalQuantity,itemType,itemPic);
        // send to server
        //sendCartData(itemId, totalQuantity);

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

    // Click on quantity to increase
    quantity.addEventListener("click", () => {
        if (totalQuantity > 0) {
            totalQuantity++;
            updateQuantity();
        }
    });

    // Initialize
    updateQuantity();
});