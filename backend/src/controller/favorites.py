from flask import request
from flask_restx import Resource
import jwt

from src.server.instance import api, db

from src.models.favorites import Favorite

from sqlalchemy import and_

from src.utils.authorization import userAuthorization
from env import JWT_KEY


@api.route('/favorite')
@api.route('/favorite/<id>')
class FavoriteRoute(Resource):
    @userAuthorization
    def post(self):
        data = api.payload
        foodId = None
        userId = jwt.decode(request.headers.get('Authorization').split()[1], JWT_KEY, algorithms="HS256")['id']
        try:
            foodId = data['foodId']
        except Exception as err:
            return {"error": "Faltando dados"}, 400

        favorite = Favorite(userId=userId, foodId=foodId)

        try:

            db.session.add(favorite)
            db.session.commit()

            response = {
                "id": favorite.id
            }

            return {"message": "Favoritado.", "data": response}, 201
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500

    @userAuthorization
    def delete(self, id):
        userId = jwt.decode(request.headers.get('Authorization').split()[1], JWT_KEY, algorithms="HS256")['id']
        try:
            favorite = Favorite.query.filter(and_(Favorite.userId == userId, Favorite.foodId == id)).first()
            db.session.delete(favorite)
            db.session.commit()

            return {"message": "Desfavoritado."}, 200
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500