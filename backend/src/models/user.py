from src.server.instance import db
from src.models.favorites import Favorite
from src.models.food import Food

class User(db.Model):
     __tablename__ = "user"

     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(20), unique=True)
     email = db.Column(db.String(254), unique=True)
     password = db.Column(db.String(100))
     admin = db.Column(db.BOOLEAN, default=False)
     active = db.Column(db.BOOLEAN, default=False)
     validationtoken = db.Column(db.String(500), nullable=True)

     favorite = db.relationship('Favorite', cascade="all, delete")
     author = db.relationship('Food', cascade="all, delete")