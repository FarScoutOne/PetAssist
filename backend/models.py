from .extensions import db


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    role = db.Column(db.String(100))

    # activities = db.relationship("Activity", back_populates="owner")


pet_food = db.Table("pet_food",
                    db.Column("pet_id", db.ForeignKey("pet.id"), primary_key=True),
                    db.Column("food_id", db.ForeignKey("food.id"), primary_key=True)
                    )


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(100))

    foods = db.relationship("Food", secondary=pet_food, back_populates="pets")
    scheduled_activities = db.relationship("ScheduledActivity", back_populates="pet")

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    flavor = db.Column(db.String(100))

    pets = db.relationship("Pet", secondary=pet_food, back_populates="foods")


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activityName = db.Column(db.String(100))
    activityDescription = db.Column(db.String(500))

    scheduled_activities = db.relationship("ScheduledActivity", back_populates="activity")


class ScheduledActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.ForeignKey("activity.id"))
    activity = db.relationship("Activity", back_populates="scheduled_activities")
    owner_id = db.Column(db.ForeignKey("owner.id"))
    pet_id = db.Column(db.ForeignKey("pet.id"))
    pet = db.relationship("Pet", back_populates="scheduled_activities")
    deadline = db.Column(db.DateTime)
