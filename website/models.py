from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db

# db.Model is a blueprint/layout for object that is to be saved in the database.
# So, due to class User, all the users must conform to the User class schema. Same with notes.

# Agriculture Class has the inputs provided in the Agriculture Class
class AgricultureInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    corn_area = db.Column(db.Integer)
    wheat_area = db.Column(db.Integer)
    soybean_area = db.Column(db.Integer)
    SG_area = db.Column(db.Integer)


    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # To associate different information with different users, we use foreign-key relationships.
    # A foreign-key is a column in one database that references a column in another database.
    # Here, we want to store the id of the user who created every note in this database.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # The above is a one-to-many relationship where there is one user with many notes.
    # Here, the user is the user class below, the lower case is because in sql, all are in lower case. 
    # the id is selected as the primary key, so we chose user.id here. if the primary key was the email for example, then we would have selected user.email.

# Energy Class has the inputs provided in the Agriculture Class
class EnergyInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    energy_value = db.Column(db.Integer)
    loan_term = db.Column(db.Integer)
    interest = db.Column(db.Integer)

    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Foreign-Key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Water Class has the inputs provided in the Agriculture Class



 