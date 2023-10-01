#Databade models

from . import db #Using . is equivalent to saying "from website import db" if referenced from outside the current directory.
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id")) #In SQL the relations or tables are stored in the name of lowercases,  i.e in this case it is stored as "user".

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key =True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #Note: Here the name of the referencing file is 'Note'(which is different from 1st case), this is how SQLAlchemy works. Only the file with a foreign key, references the main relation in terms of its lower case name.

    


