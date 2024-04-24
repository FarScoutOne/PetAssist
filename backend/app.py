from flask import Flask, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    role = db.Column(db.String(100))

    activities = db.relationship("Activity", back_populates="owner")

pet_food = db.Table("pet_food",
                    db.Column("pet_id", db.ForeignKey("pet.id"), primary_key=True),
                    db.Column("food_id", db.ForeignKey("food.id"), primary_key=True)
                    )

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(100))

    activities = db.relationship("Activity", back_populates="pet")
    foods = db.relationship("Food", secondary=pet_food, back_populates="pets")

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activityName = db.Column(db.String(100))
    activityDescription = db.Column(db.String(500))
    equipmentNeeded = db.Column(db.String(500))
    owner_id = db.Column(db.ForeignKey("owner.id"))
    pet_id = db.Column(db.ForeignKey("pet.id"))

    owner = db.relationship("Owner", back_populates="activities")
    pet = db.relationship("Pet", back_populates="activities")

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    flavor = db.Column(db.String(100))

    pets = db.relationship("Pet", secondary=pet_food, back_populates="foods")


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


def insert_data():
    husband = Owner(name="Ryne", age="38", role="parent")
    wife = Owner(name="Samantha", age=34, role="parent")
    cat_pet = Pet(name="Kit", type="cat")
    db.session.add_all([husband, wife, cat_pet])

    new_activity = Activity(activityName="feed", activityDescription="Feed one can of wet food and one scoop of dry food.", equipmentNeeded="1 can of wet food, dry food",owner=husband, pet=cat_pet)
    play_activity = Activity(activityName="play", activityDescription="Play indoors and get him to run around and catch.", equipmentNeeded="toys", owner=wife, pet=cat_pet)
    
    db.session.add_all([new_activity, play_activity])
    db.session.commit()

def update_first_owner():
    owner = Owner.query.first()
    owner.name = 'Ryken'
    db.session.commit()

def delete_first_owner():
    owner = Owner.query.first()
    db.session.delete(owner)
    db.session.commit()

def query_tables():
    first_owner = Owner.query.first()

    print("First Owner")
    for activity in first_owner.activities:
        print(f"Activity: {activity.activityName}  Pet: {activity.pet_id}")

    print("Second Owner")
    second_owner = Owner.query.filter_by(id=2).first()

    for activity in second_owner.activities:
        print(f"Activity: {activity.activityName}  Pet: {activity.pet_id}")

def add_foods_to_pets():
    first_food = Food(brand="Fancy Feast", flavor="Turkey Delight")
    second_food = Food(brand="Blue Wilderness", flavor="Alaskan Salmon")

    first_pet = Pet.query.first()
    first_pet.foods.append(first_food)
    first_pet.foods.append(second_food)

    db.session.add_all([first_food, second_food])
    db.session.commit()

def query_pet_foods():
    first_pet = Pet.query.filter_by(name="Kit").first()

    print("Kit's Food")
    for food in first_pet.foods:
        print(f"Food: {food.brand}: {food.flavor}")

def get_all_owners():
    owners = Owner.query.all()

    for owner in owners:
        print(f"Owner name: {owner.name}")

    owner_count = Owner.query.count()
    print(f"Owner count: {owner_count}")
    