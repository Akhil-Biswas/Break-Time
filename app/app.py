from flask import Flask

# Blueprints
from app.users import user
from app.auth import auth

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

app.register_blueprint(user)
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")