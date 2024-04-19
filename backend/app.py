from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello</h1>"


@app.route("/home")
def home():
    return "<h1>Home</h1>"


@app.route("/json")
def json():
    return {"mykey": "JSON Value!", "mylist": [1, 2, 3, 4, 5]}
