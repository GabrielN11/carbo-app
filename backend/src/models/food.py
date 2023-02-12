from src.server.instance import db
from sqlalchemy import Enum
from src.models.enum.measure import Measure
from src.models.enum.measuretype import MeasureType
from src.models.favorites import Favorite

class Food(db.Model):
     __tablename__ = "food"

     id = db.Column(db.Integer, primary_key=True)
     carbo = db.Column(db.Numeric(10, 2))
     measure = db.Column(Enum(Measure), nullable=True)
     measureQuantity = db.Column(db.Integer, nullable=True)
     name = db.Column(db.String(50))
     description = db.Column(db.String(500), nullable=True)
     quantity = db.Column(db.Numeric(10, 2), nullable=True)
     quantityType = db.Column(Enum(MeasureType))
     active = db.Column(db.BOOLEAN, default=False)
     author = db.Column(db.Integer, db.ForeignKey('user.id'))

     favorite = db.relationship('Favorite', cascade="all, delete")