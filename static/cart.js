// store in localstorage
function saveCartData(itemId,quantity) {
    // Get existing cart or initialize empty
    let cart = JSON.parse(localStorage.getItem("Cart")) || {};

    // If quantity <= 0, remove the item
    if (quantity <= 0) {
        delete cart[itemId];
    } else {
        // Otherwise add/update the item
        cart[itemId].quantity= quantity;
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

function orderPlace(){
    const cart = JSON.parse(localStorage.getItem("Cart") || "{}");
    //checking item present or not
    if (Object.keys(cart).length){
        //send data to server
        fetch("/orderPlaced", {
            method: "POST",
            headers: {
            "Content-Type": "application/json"
            },
            body: localStorage.getItem("Cart")
        })
        .then(response => response.json())//convert into  json
        .then(data => {
            console.log(data)
            if (data.status ==="success"){
                console.info(data.message);
                alert("Order Placed")
            }else if (data.status ==="error"){
                console.info(data.message);
                alert("Error..")
            }
        })
        .then(
            // cleare localStorage
            )
    }else{
        console.warn("cart is empty")
        window.location.reload()
        alert("cart is empty")
    }
}

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
        <div class="removeItem">
            <img class="delItem" src="../static/src/delete-icon.svg" alt="Remove Item" />
        </div>
    `;

    return itemCard;
}

function createConfirmBtn(grandTotalPrice){
    console.info(grandTotalPrice)
    
    const confirmOrder = document.querySelector("#confirmOrder");
    confirmOrder.innerHTML = `
    <div id="grendTotal">
        <span>Total</span>
        <span>₹${grandTotalPrice}</span>
    </div>
    <div id="orderSubmitBtn">
        <button type="submit">Place Order
        </button>
    </div>`
    
    // order to server 
    const orderbtn = document.querySelector("#orderSubmitBtn button")

orderbtn.addEventListener("click",orderPlace)
}
// Select all addToCart containers
let sevedItem = JSON.parse(localStorage.getItem("Cart"));
let grandTotalPrice = 0

function cartlogic(itemCard,sevedItem){
    const itemId = itemCard.getAttribute("item-id");
    const itemName = itemCard.querySelector(".itemName").textContent.trim();
    const itemType = itemCard.querySelector(".itemType").alt;
    const itemPic = itemCard.querySelector(".itemPic").src;
    const cartbtn = itemCard.querySelector(".addTocart");

    const removeItem = cartbtn.querySelector(".removeItem");
    const quantity = cartbtn.querySelector(".quantity");
    const addItem = cartbtn.querySelector(".addItem");
    const totalPrice = itemCard.querySelector(".total p");
    const delItem = itemCard.querySelector(".delItem");

    let cartdata = JSON.parse(localStorage.getItem("Cart"))
    let totalQuantity = cartdata[itemId].quantity ||0 ; //first check in localstorage if not then quantity is 0
    
    // calculte price of the item Client side 
    const itemPriceDisplay = itemCard.querySelector(".itemPrice");
    const itemPrice= parseFloat(itemPriceDisplay.textContent.replace('₹',''));
    
    
    const totalItemPrice =itemPrice*totalQuantity;
    //uptdate price 
    function updatePrice(){
        totalPrice.textContent = `₹${itemPrice * totalQuantity}`;
    }
    
    function updateQuantity() {
        quantity.textContent = totalQuantity;
        // updated price
            updatePrice();
            
            
        console.log(itemId, totalQuantity);
        // store in localstorage
        saveCartData(itemId,totalQuantity);
        
        // send to server
        //sendCartData(itemId, totalQuantity);

        if (totalQuantity === 0) {
            itemCard.remove()
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
            updatePrice();
        }
    });

    // Delete button
    delItem.addEventListener("click", () => {
        totalQuantity = 0;
        updateQuantity();
    });

    // Initialize
    updateQuantity();
}

window.addEventListener("load", () => {
    const savedCart = JSON.parse(localStorage.getItem("Cart")) || {};
    const container = document.getElementById("cartlist");

    if (Object.keys(savedCart).length > 0) {
      
        document.querySelector("#emptyCartDisplay").style.display = 'none'
        
        // There are items in the cart, create cards
        Object.entries(savedCart).forEach(([id, item]) => {
            const itemCard = createItemCard({
                id: id,
                name: item.itemName,
                price: item.itemPrice,
                type: item.itemType,
                quantity: item.quantity,
                image: item.itemPic
            });
            
            container.appendChild(itemCard);
            cartlogic(itemCard);
            grandTotalPrice +=parseFloat(item.itemPrice*item.quantity);
    
        });
        createConfirmBtn(grandTotalPrice);
    } else {
        document.querySelector("#confirmOrder").style.display ="none"
        document.querySelector("#emptyCartDisplay").style.display = 'flex'
    }
});


/*
 // change ui if cart is empty then show emply ui
    if (Object.keys(savedCart).length === 0) {
        document.querySelector("#confirmOrder").style.display ="none"
        document.querySelector("#emptyCartDisplay").style.display = 'flex'
    } else {
        document.querySelector("#confirmOrder").style.display ="flex"
        document.querySelector("#emptyCartDisplay").style.display = 'none'
    } 
*/
