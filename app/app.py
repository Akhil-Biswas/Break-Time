from flask import Flask, render_template, url_for
from flask import redirect
app = Flask(__name__)

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
    return coming_soon

def login():
    return coming_soon


@app.route("/signup/" ,methods=["GET","POST"])
def signup():
    return coming_soon

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")