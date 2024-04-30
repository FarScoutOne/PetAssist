from .extensions import db


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


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    flavor = db.Column(db.String(100))

    pets = db.relationship("Pet", secondary=pet_food, back_populates="foods")


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activityName = db.Column(db.String(100))
    activityDescription = db.Column(db.String(500))
    equipmentNeeded = db.Column(db.String(500))
    owner_id = db.Column(db.ForeignKey("owner.id"))
    pet_id = db.Column(db.ForeignKey("pet.id"))

    owner = db.relationship("Owner", back_populates="activities")
    pet = db.relationship("Pet", back_populates="activities")


class ScheduledActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.ForeignKey("activity.id"))
    owner_id = db.Column(db.ForeignKey("owner.id"))
    pet_id = db.Column(db.ForeignKey("pet.id"))
    deadline = db.Column(db.DateTime)
