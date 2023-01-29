from src.server.instance import db

class Favorite(db.Model):
     __tablename__ = "favorite"

     id = db.Column(db.Integer, primary_key=True)
     foodId = db.Column(db.Integer, db.ForeignKey('food.id'))
     userId = db.Column(db.Integer, db.ForeignKey('user.id'))