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

    console.info("Cart saved:");
    console.table(cart);
}

// Select all addTocart containers
const carts = document.querySelectorAll(".addTocart");

carts.forEach(cart => {
    const itemCard = cart.closest(".itemCard"); // find parent card

    const itemId = parseInt(itemCard.getAttribute("item-id"));
    const itemName = itemCard.querySelector(".itemName").textContent.trim();
    const itemPrice = parseFloat(itemCard.querySelector(".itemPrice").textContent.replace('₹','').trim());
        //url: static/src/itemType.svg
    const itemType = itemCard.getAttribute("item-type");
    const itemPic =itemCard.querySelector(".itemPic").src;
    const removeItem = cart.querySelector(".removeItem");
    const quantity = cart.querySelector(".quantity");
    const addItem = cart.querySelector(".addItem");

    let cartData = JSON.parse(localStorage.getItem("Cart")) || {};
    let totalQuantity = cartData[itemId] ? cartData[itemId].quantity : 0;    //first check in localstorage if not then quantity is 0

    function updateQuantity() {
        quantity.textContent = totalQuantity;
        console.log(itemId, totalQuantity);
        // store in localstorage
        saveCartData(itemId,itemName,itemPrice,totalQuantity,itemType,itemPic);
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
    
    // Initialize
    updateQuantity();
});