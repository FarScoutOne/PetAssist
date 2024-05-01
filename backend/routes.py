from flask import Blueprint, request, jsonify, redirect

from .models import Owner, Pet, Food, Activity, ScheduledActivity
from .extensions import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "<h1>This is from the Blueprint</h1>"


@main.route("/owners")
def get_owners():
    owners = Owner.query.all()

    owner_list = []
    for owner in owners:
        owner_dict = {
            "name": owner.name,
            "age": owner.age,
            "role": owner.role
        }
        owner_list.append(owner_dict)

    return jsonify({"owners": owner_list})


@main.route("/owners/<int:owner_id>")
def get_owner(owner_id):
    owner = Owner.query.get_or_404(owner_id)
    owner_dict = {
        "name": owner.name,
        "age": owner.age,
        "role": owner.role
    }
    return jsonify(owner_dict)


@main.route("/add_owner", methods=['POST'])
def add_owner():
    data = request.get_json()

    new_owner = Owner(name=data['name'], age=data['age'], role=data['role'])
    db.session.add(new_owner)
    db.session.commit()

    return jsonify({"message": "Owner added"}), 201


@main.route('/owner/<int:id>', methods=['DELETE'])
def delete_owner(id):
    owner_to_delete = Owner.query.get_or_404(id)
    try:
        db.session.delete(owner_to_delete)
        db.session.commit()
        return redirect('/owners')
    except:
        return 'There was a problem deleting that owner'


@main.route("/pets")
def get_all_pets():
    pets = Pet.query.all()

    pet_list = []
    for pet in pets:
        pet_dict = {
            "name": pet.name,
            "type": pet.type
        }
        pet_list.append(pet_dict)

    return jsonify({"pets": pet_list})


@main.route("/add_pet", methods=['POST'])
def add_pet():
    data = request.get_json()

    new_pet = Pet(name=data['name'], type=data['type'])
    db.session.add(new_pet)
    db.session.commit()

    return jsonify({"message": "Pet added"}), 201


@main.route("/pets/<int:pet_id>", methods=['GET'])
def get_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    pet_dict = {
        "name": pet.name,
        "type": pet.type
    }
    return jsonify(pet_dict)


@main.route('/pet/<int:id>', methods=['DELETE'])
def delete_pet(id):
    pet_to_delete = Pet.query.get_or_404(id)
    try:
        db.session.delete(pet_to_delete)
        db.session.commit()
        return redirect('/pets')
    except:
        return 'There was a problem deleting that owner'


@main.route("/add_food", methods=['POST'])
def add_food():
    data = request.get_json()

    new_food = Food(brand=data['brand'], flavor=data['flavor'])
    db.session.add(new_food)
    db.session.commit()

    return jsonify({"message": "Food added"}), 201


@main.route("/foods")
def get_all_foods():
    foods = Food.query.all()

    food_list = []
    for food in foods:
        food_dict = {
            "brand": food.brand,
            "flavor": food.flavor
        }
        food_list.append(food_dict)

    return jsonify({"foods": food_list})


@main.route("/foods/<int:food_id>", methods=['GET'])
def get_food(food_id):
    food = Food.query.get_or_404(food_id)
    food_dict = {
        "brand": food.brand,
        "flavor": food.flavor
    }
    return jsonify(food_dict)


@main.route("/foods/<int:food_id>", methods=['DELETE'])
def delete_food(food_id):
    food_to_delete = Food.query.get_or_404(food_id)
    try:
        db.session.delete(food_to_delete)
        db.session.commit()
        return redirect('/foods')
    except:
        return 'There was a problem deleting that food'


@main.route("/add_food_to_pet", methods=['POST'])
def add_food_to_pet():
    data = request.get_json()

    pet_id = data['pet_id']
    food_id = data['food_id']

    pet = Pet.query.get(pet_id)
    food = Food.query.get(food_id)

    pet.foods.append(food)
    db.session.commit()

    return jsonify({"message": "Food added to pet"}), 201


@main.route("/activities")
def get_all_activities():
    activities = Activity.query.all()

    activity_list = []
    for activity in activities:
        activity_dict = {
            "name": activity.activityName,
            "description": activity.activityDescription,
            "equipment": activity.equipmentNeeded
        }
        activity_list.append(activity_dict)

    return jsonify({"activities": activity_list})


@main.route("/add_activity", methods=['POST'])
def add_activity():
    data = request.get_json()

    new_activity = Activity(activityName=data['activityName'], activityDescription=data['activityDescription'],
                            equipmentNeeded=data['equipmentNeeded'])
    db.session.add(new_activity)
    db.session.commit()

    return jsonify({"message": "Activity added"}), 201


@main.route("/activities/<int:activity_id>", methods=['GET'])
def get_activity(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    activity_dict = {
        "name": activity.activityName,
        "description": activity.activityDescription,
        "equipment": activity.equipmentNeeded
    }
    return jsonify(activity_dict)


@main.route("/update_owner/<int:owner_id>", methods=['PUT'])
def update_owner(owner_id):
    owner = Owner.query.get_or_404(owner_id)
    data = request.get_json()

    owner.name = data['name']
    owner.age = data['age']
    owner.role = data['role']

    db.session.commit()

    return jsonify({"message": "Owner updated"}), 200


@main.route("/activities/<int:activity_id>", methods=['DELETE'])
def delete_activity(activity_id):
    activity_to_delete = Activity.query.get_or_404(activity_id)
    try:
        db.session.delete(activity_to_delete)
        db.session.commit()
        return redirect('/activities')
    except:
        return 'There was a problem deleting that activity'


@main.route("/update_pet/<int:pet_id>", methods=['PUT'])
def update_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    data = request.get_json()

    pet.name = data['name']
    pet.type = data['type']

    db.session.commit()

    return jsonify({"message": "Pet updated"}), 200


@main.route("/update_food/<int:food_id>", methods=['PUT'])
def update_food(food_id):
    food = Food.query.get_or_404(food_id)
    data = request.get_json()

    food.brand = data['brand']
    food.flavor = data['flavor']

    db.session.commit()

    return jsonify({"message": "Food updated"}), 200


@main.route("/update_activity/<int:activity_id>", methods=['PUT'])
def update_activity(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    data = request.get_json()

    activity.activityName = data['activityName']
    activity.activityDescription = data['activityDescription']
    activity.equipmentNeeded = data['equipmentNeeded']

    db.session.commit()

    return jsonify({"message": "Activity updated"}), 200


@main.route("/scheduled_activities", methods=['GET'])
def get_scheduled_activities():
    scheduled_activities = ScheduledActivity.query.all()

    scheduled_activities_list = []
    for activity in scheduled_activities:
        activity_dict = {
            "activity_id": activity.activity_id,
            "pet_id": activity.pet_id,
            "time": activity.time
        }
        scheduled_activities_list.append(activity_dict)

    return jsonify({'scheduled_activities': scheduled_activities_list})


@main.route("/update_scheduled_activity/<int:scheduled_activity_id>", methods=['PUT'])
def update_scheduled_activity(scheduled_activity_id):
    scheduled_activity = ScheduledActivity.query.get_or_404(scheduled_activity_id)
    data = request.get_json()

    scheduled_activity.activity_id = data['activity_id']
    scheduled_activity.pet_id = data['pet_id']
    scheduled_activity.time = data['time']

    db.session.commit()

    return jsonify({"message": "Scheduled Activity updated"}), 200


@main.route("/update_scheduled_activity/<int:scheduled_activity_id>", methods=['DELETE'])
def delete_scheduled_activity(scheduled_activity_id):
    scheduled_activity = ScheduledActivity.query.get_or_404(scheduled_activity_id)
    try:
        db.session.delete(scheduled_activity)
        db.session.commit()
        return redirect('/scheduled_activities')
    except:
        return 'There was a problem deleting that scheduled activity'


def insert_data():
    # Add pet owners
    new_owner1 = Owner(name="Bob", age="38", role="parent")
    new_owner2 = Owner(name="Alice", age=34, role="parent")
    new_owner3 = Owner(name="Charlie", age=12, role="child")

    db.session.add_all([new_owner1, new_owner2, new_owner3])
    db.session.commit()

    # Add pets
    new_pet1 = Pet(name="Spot", type="dog")
    new_pet2 = Pet(name="Bruiser", type="dog")
    new_pet3 = Pet(name="Whiskers", type="cat")

    db.session.add_all([new_pet1, new_pet2, new_pet3])
    db.session.commit()

    # Add pet food
    new_food1 = Food(brand="Fancy Feast", flavor="Turkey Delight")
    new_food2 = Food(brand="Iams", flavor="Venison")
    new_food3 = Food(brand="Blue Wilderness", flavor="Alaskan Salmon")

    # Assign food to pets
    new_pet1.foods.append(new_food2)
    new_pet2.foods.append(new_food2)
    new_pet3.foods.append(new_food1)
    new_pet3.foods.append(new_food3)

    db.session.add_all([new_food1, new_food2, new_food3])
    db.session.commit()

    # Add activities
    feed_activity = Activity(activityName="feed",
                             activityDescription="Feed one can of wet food and one scoop of dry food.",
                             equipmentNeeded="1 can of wet food, dry food", owner=new_owner1, pet=new_pet3)
    play_activity = Activity(activityName="play",
                             activityDescription="Play indoors and get him to run around and catch.",
                             equipmentNeeded="toys", owner=new_owner3, pet=new_pet1)

    db.session.add_all([feed_activity, play_activity])
    db.session.commit()

# def query_tables():
#     first_owner = Owner.query.first()
#
#     print("First Owner")
#     for activity in first_owner.activities:
#         print(f"Activity: {activity.activityName}  Pet: {activity.pet_id}")
#
#     print("Second Owner")
#     second_owner = Owner.query.filter_by(id=2).first()
#
#     for activity in second_owner.activities:
#         print(f"Activity: {activity.activityName}  Pet: {activity.pet_id}")
#
#
# def query_pet_foods():
#     first_pet = Pet.query.filter_by(name="Spot").first()
#
#     print("Spot's Food")
#     for food in first_pet.foods:
#         print(f"Food: {food.brand}: {food.flavor}")
#
#
# def get_all_owners():
#     owners = Owner.query.all()
#
#     for owner in owners:
#         print(f"Owner name: {owner.name}")
#
#     owner_count = Owner.query.count()
#     print(f"Owner count: {owner_count}")
