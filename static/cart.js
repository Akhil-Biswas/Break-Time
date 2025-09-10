function saveCartData(itemId, quantity) {
    // Get existing cart or initialize empty
    let cart = JSON.parse(localStorage.getItem("Cart")) || {};

    // If quantity <= 0, remove the item
    if (quantity <= 0) {
        delete cart[itemId];
    } else {
        // Otherwise add/update the item
        cart[itemId].quantity = quantity;
    }
    // Save updated cart back to localStorage
    localStorage.setItem("Cart", JSON.stringify(cart));
    console.info("Cart saved:");
    console.table(cart);
}
// HTML component
function createItemCard(item) {
    const itemCard = document.createElement("div");
    itemCard.setAttribute("item-id", item.id);
    itemCard.classList.add("item");

    itemCard.innerHTML = `
        <div class="pic">
            <img class="itemPic" src="${item.image}" alt="item" />
            <img class="itemType" src="../static/src/${item.type}.svg" alt="${item.type}" />
        </div>
        <div class="namePrice">
            <p class="itemName">${item.name}</p>
            <p class ="itemPrice">₹${item.price}</p>
        </div>
        <div class="quantitycontainer">
            <div class="addTocart">
                <span class="removeItem">
                    <img src="../static/src/minus-circle.svg" alt="remove item" />
                </span>
                <span class="quantity">0</span>
                <span class="addItem">
                    <img src="../static/src/plus-circle.svg" alt="add item"/>
                </span>
            </div>
        </div>
        <div class="total">
            <p>₹0</p>
        </div>
        <div class="delItem">
            <img class="delItem" src="../static/src/delete-icon.svg" alt="Remove Item" />
        </div>
    `;

    return itemCard;
};
function createConfirmBtn(grandTotalPrice){
    console.info(grandTotalPrice)

    const confirmOrder = document.querySelector("#confirmOrder");
    confirmOrder.innerHTML = `
    <div id="grandTotal">
        <span>Total</span>
        <span>₹${grandTotalPrice}</span>
    </div>
    <div id="orderSubmitBtn">
        <button type="submit">Place Order
        </button>
    </div>`
};

// Select all addToCart containers
const carts = document.querySelectorAll(".addTocart");

carts.forEach(cart => {
    const itemCard = cart.closest(".item"); // find parent card
    const itemId = parseInt(itemCard.getAttribute("item-id"));

    const removeItem = cart.querySelector(".removeItem");
    const quantity = cart.querySelector(".quantity");
    const addItem = cart.querySelector(".addItem");
    const delItem = itemCard.querySelector(".delItem");

    let cartData = JSON.parse(localStorage.getItem("Cart")) || {};
    let totalQuantity = cartData[itemId] ? cartData[itemId].quantity : 0;    //first check in localstorage if not then quantity is 0

    function updateQuantity() {
        quantity.textContent = totalQuantity;

        console.log(itemId, totalQuantity);
        // store in localstorage
        saveCartData(itemId, totalQuantity);
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

//++ Dummy Data ++
const item1 = {
    id:2,
    name: "Noodles",
    image: "http://localhost:5000/static/.images/items/noodles.jpeg",
    price: 70,
    type: "veg",
    quantity: 2
}
const item2 = {
    id:3,
    name: "Hot Dogs",
    image: "http://localhost:5000/static/.images/items/noodles.jpeg",
    price: 50,
    type: "veg",
    quantity: 3
}
//-- Dummy Data --
const container = document.getElementById("cartlist");
// Creating list using list component
const itemCard1 = createItemCard(item1)
const itemCard2 = createItemCard(item2)
// appending in list
container.appendChild(itemCard1)
container.appendChild(itemCard2)

createConfirmBtn(100);