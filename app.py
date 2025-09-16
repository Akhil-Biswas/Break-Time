from flask import Flask, render_template, url_for
from flask import request 
from flask import redirect
from flask import session
from flask import jsonify
from db import User, Login
from items import Items
from saveimage import saveimage
from datetime import timedelta
from config import Folders
app = Flask(__name__)

app.secret_key ="namaste"
app.permanent_session_lifetime = timedelta(days=7)  # session expires in 7 days

# categories
categories= [{"name": "Sandwich", "img":"sandwich.png"},{"name": "Noodles", "img":"noodles.jpeg"},{"name": "Hotdog", "img":"Hotdog.jpg"},{"name": "Bread", "img":"bread.jpeg"},{"name": "Roti", "img":"roti.jpeg"},{"name": "rice", "img":"Rice.jpeg"}]

#items


@app.route("/")
def home():
    return render_template("index.html", categories=categories, items=Items.getAllItem())
    
@app.route("/Favourite/")
def favourite():
    return coming_soon
@app.route("/Search/")
def search():
    return coming_soon
    
@app.route("/Cart/")
def cart():
    
    return render_template("cart.html")
    
@app.route("/orderPlaced", methods =["POST"])
def orderAccept():
    if 'user' in session:
        if request.method == "POST":
            data = request.get_json()
            print(type(data))
            if not data:
                response ={"status": "error",
                 "message": "Cart is empty"}
                return jsonify(response),400
            else:
                response ={"status": "success",
                 "message": "Order received"}
                return jsonify(response),200
    else:
        return redirect(url_for("login"))
@app.route("/update_cart", methods=["POST"])
def addToCart():
    data = request.get_json()
    itemid = data["itemid"]
    quantity = data ["quantity"]
    print (itemid,quantity)
    #app.logger.info(f"Item ID: {itemid}, Quantity: {quantity}")
    return jsonify({
            "status": "success",
            "message": "Cart updated"})
    
    
@app.route("/cr/")
def crpage():
    return coming_soon
    return render_template("cr/index.html")
    
@app.route("/restaurant/")
def restaurantpage():
    return render_template("restaurant/index.html")
    
@app.route("/restaurant/additems",methods =["GET", "POST"])
def additem():
    app.config["FOLDER_NAME"] = Folders.Items_Photo
    if request.method =="POST":
    
        item = Items(
        itemId = None, #Database will autometic genarate (By Autoincreament)
        itemName = request.form['itemName'],
        itemPrice = request.form['itemPrice'],
        vegFlag = request.form['vegFlag'],
        category = 1,
        restaurant = 1
        ).saveItemInDatabase() #now item store item id
        
       # access file object
        file = request.files['itemImage']
        fileName = saveimage(app.config["FOLDER_NAME"],file,item)
       
    return render_template("restaurant/additem.html")

# other
coming_soon = '<div style="display:flex;justify-content:center;align-items:center;height:100vh;"><h1>Coming Soon......</h1></div> '
@app.route("/AboutUs/")
def aboutus():
    # return render_template("me.html")
    return coming_soon
    
@app.route("/contribute/")
def report():
    return coming_soon
    
@app.route("/contectMe/")
def me():
    return coming_soon
    
@app.route("/profile")
def profile():
    if 'user' not in session:
        return redirect(url_for("login"))
    user = session['user'] 
    return render_template("profile.html",user = user)
@app.route("/signup/" ,methods=["GET","POST"])
def signup():
    if request.method =="POST":
        user= User(
        userid = None, #Database will autometic genarate (By Autoincreament)
        fname = request.form['fname'],
        mname = request.form['mname'],
        lname = request.form['lname'],
        departmentid = request.form['departmentid'],
        #--- semister
        sectionid = request.form['sectionid'],
        tel = request.form['tel'],
        email = request.form['email'],
        password = request.form['pass']
        )
        #save in database
        user.saveindatabase()
        # Create session
        session.permanent = True
        session['user'] = {
            "userid":user.userid,
            "fname": user.fname,
            "mname": user.mname,
            "lname": user.lname,
            "departmentid": user.departmentid,
            "sectionid": user.sectionid,
            "tel": user.tel,
            "email": user.email
        }
        return redirect(url_for("login"))
      
    return render_template("login/signup.html")
    
@app.route("/login/" ,methods=["GET","POST"])
def login():
    if request.method == "POST":
        tel = request.form['tel']
        password = request.form['pass']
        
        login=Login(tel,password)
        data = login.authenticate() #from database
        if data :
            user= User(
        userid = data[0],
        fname = data[1],
        mname = data[2],
        lname = data[3],
        departmentid = data[4],
        sectionid = data[5],
        tel = data[6],
        email = data[7],
        password = ''
        )    
            session.permanent = True
            session['user'] = {
            "userid":user.userid,
            "fname": user.fname,
            "mname": user.mname,
            "lname": user.lname,
            "departmentid": user.departmentid,
            "sectionid": user.sectionid,
            "tel": user.tel,
            "email": user.email
        }
        
            return redirect(url_for("profile"))
        
    return render_template("login/login.html")


    
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")