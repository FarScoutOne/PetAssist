from flask import Flask, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "<h1>Hello</h1>"

@app.route("/home", methods=["GET"])
def home():
    return "<h1>Home</h1>"

@app.route("/json")
def json():
    return {"mykey": "JSON Value!", "mylist": [1, 2, 3, 4, 5]}

@app.route("/dynamic", defaults={"user_input": "default"})
@app.route("/dynamic/<user_input>")
def dynamic(user_input):
    return f"<h1>The user entered: {user_input}</h1>"

@app.route("/query")
def query():
    first = request.args.get("first")
    second = request.args.get("second")
    return f"<h1>The query string contains: {first} and {second}</h1>"

@app.route("/acceptjson")
def acceptjson():
    json_data = request.get_json()
    api_input = json_data["mylist"]
    hello = json_data["hello"]
    return {"api_input": api_input, "hello": hello}
