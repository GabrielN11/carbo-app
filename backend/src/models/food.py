from src.server.instance import db
from sqlalchemy import Enum
from src.models.enum.measure import Measure

class Food(db.Model):
     __tablename__ = "food"

     id = db.Column(db.Integer, primary_key=True)
     carbo = db.Column(db.Numeric(10, 2))
     measure = db.Column(Enum(Measure))
     name = db.Column(db.String(50))
     description = db.Column(db.String(500))
     quantity = db.Column(db.Numeric(10, 2))
     active = db.Column(db.BOOLEAN, default=False)
     author = db.Column(db.Integer, db.ForeignKey('user.id'))

     favorite = db.relationship('Favorite', cascade="all, delete")