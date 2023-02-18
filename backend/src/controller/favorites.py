from flask import request
from flask_restx import Resource
import jwt

from src.server.instance import api, db


from src.models.favorites import Favorite
from src.models.user import User
from src.models.food import Food


from sqlalchemy import and_, desc

from src.utils.authorization import userAuthorization
from env import JWT_KEY

from src.models.enum.measure import Measure
from src.models.enum.measuretype import MeasureType


@api.route('/favorite')
@api.route('/favorite/<id>')
class FavoriteRoute(Resource):
    def get(self, id):
        limit = 10
        page = 0
        try:
            page = int(request.args.get('page')) * 10
        except:
            return {"error": "Page not informed correctly."}, 400

        user = User.query.filter_by(id=id).first()
        if user.active == False:
            return {"error": "This user is banned."}, 403

        try:
            currentUserId = None
            try:
                currentUserId = jwt.decode(request.headers.get('Authorization').split()[1], JWT_KEY, algorithms="HS256")['id']
            except:
                currentUserId = -1

            favorites = Favorite.query.filter_by(userId=id).order_by(desc(Favorite.id)).limit(limit).offset(page).all()

            def getContent(favorite):
                food = Food.query.filter_by(id=favorite.foodId).first()
                isFavorite = Favorite.query.filter(and_(Favorite.userId == currentUserId, Favorite.foodId == food.id)).first()

                response = {
                    "id": food.id,
                    "name": food.name,
                    "description": None if not food.description else food.description,
                    "carbo": float(food.carbo),
                    "quantity": None if not food.quantity else float(food.quantity),
                    "measure": None if not food.measure else Measure(food.measure).value,
                    "measureQuantity": None if not food.measureQuantity else int(food.measureQuantity),
                    "quantityType": MeasureType(food.quantityType).value,
                    "isFavorite": bool(isFavorite),
                    "user": {
                        "id": user.id,
                        "name": user.username
                    }
                }
                return response

            content = list(map(getContent, favorites))

            return {"message": "Shares retrieved.", "data": content}, 200
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500

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