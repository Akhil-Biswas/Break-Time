from flask import Flask, render_template, url_for
from flask import redirect
from flask import request 
from flask import session
from datetime import timedelta
from db import User, Login
from config import Session

app = Flask(__name__)

app.secret_key =Session.secret_key
app.permanent_session_lifetime = timedelta(days=7)  # session expires in 7 days

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/favourite/")
def favourite():
    return coming_soon
@app.route("/search/")
def search():
    return coming_soon
    
@app.route("/cart/")
def cart():
    return coming_soon

@app.route("/cr/")
def crpage():
    return coming_soon
    
@app.route("/restaurant/")
def restaurantpage():
    return coming_soon

# other
coming_soon = '<div style="display:flex;justify-content:center;align-items:center;height:100vh;"><h1>Coming Soon......</h1></div> <script> alert("Coming Soon......");</script>'

@app.route("/aboutus/")
def aboutus():
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
    username = session['user']["fname"]
    return render_template("profile.html",user = username)
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