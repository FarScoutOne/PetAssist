from flask import Blueprint

from.models import Owner,pet_food, Pet, Food, Activity
from .extensions import db

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return "<h1>This is from the Blueprint</h1>"

@main.route("/acceptjson")
def acceptjson():
    json_data = request.get_json()
    api_input = json_data["mylist"]
    hello = json_data["hello"]
    return {"api_input": api_input, "hello": hello}

def insert_data():
    husband = Owner(name="Bob", age="38", role="parent")
    wife = Owner(name="Alice", age=34, role="parent")
    cat_pet = Pet(name="Spot", type="cat")
    db.session.add_all([husband, wife, cat_pet])

    new_activity = Activity(activityName="feed", activityDescription="Feed one can of wet food and one scoop of dry food.", equipmentNeeded="1 can of wet food, dry food",owner=husband, pet=cat_pet)
    play_activity = Activity(activityName="play", activityDescription="Play indoors and get him to run around and catch.", equipmentNeeded="toys", owner=wife, pet=cat_pet)
    
    db.session.add_all([new_activity, play_activity])
    db.session.commit()

def update_first_owner():
    owner = Owner.query.first()
    owner.name = 'Charlie'
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
    first_pet = Pet.query.filter_by(name="Spot").first()

    print("Spot's Food")
    for food in first_pet.foods:
        print(f"Food: {food.brand}: {food.flavor}")

def get_all_owners():
    owners = Owner.query.all()

    for owner in owners:
        print(f"Owner name: {owner.name}")

    owner_count = Owner.query.count()
    print(f"Owner count: {owner_count}")

