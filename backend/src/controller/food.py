from flask import request
from flask_restx import Resource
from datetime import datetime, timedelta
import jwt

from src.models.food import Food
from src.models.enum.measure import Measure

from sqlalchemy import desc, func, or_

from src.server.instance import api, db
from decimal import Decimal

from src.models.user import User

from src.utils.authorization import userAuthorization
from env import JWT_KEY


@api.route('/food')
@api.route('/food/<id>')
class FoodRoute(Resource):
    @userAuthorization
    def post(self):
        data = api.payload
        carbo = None
        measure = None
        measureQuantity = None
        name = None
        description = None
        quantity = None
        author = None

        try:
            carbo = data['carbo']
            measure = data['measure']
            measureQuantity = data['measureQuantity']
            name = data['name']
            description = data['description'] or ''
            quantity = data['quantity']
            author = data['userId']
        except Exception as err:
            try:
                carbo = data['carbo']
                name = data['name']
                author = data['userId']
            except Exception as err:
                return {"error": "Faltando dados"}, 400

        if (description != None) and (len(description) > 500):
            return {"error": "Descrição muito longa."}, 400

        if (measure != None and measureQuantity == None) or (measureQuantity == None and measure != None):
            return {"error": "Necessário informar medida e quantidade de medida."}, 400


        food = Food(carbo=carbo, name=name, description=description, quantity=quantity, author=author)
        try:
            if measure != None:
                food.measure = Measure(measure)

            db.session.add(food)
            db.session.commit()

            response = {
                "id": food.id,
            }

            return {"message": "Alimento postado.", "data": response}, 201
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500

    @userAuthorization
    def put(self, id):
        data = api.payload
        carbo = None
        measure = None
        name = None
        description = None
        quantity = None

        try:
            carbo = data['carbo']
            measure = data['measure']
            measureQuantity = data['measureQuantity']
            name = data['name']
            description = data['description'] or ''
            quantity = data['quantity']
        except Exception as err:
            return {"error": "Missing data."}, 400

        if len(description) > 500:
            return {"error": "Descrição muito longa."}, 400

        if (not measure and measureQuantity) or (not measureQuantity and measure):
            return {"error": "É necessário haver uma quantidade e medida"}, 400

        try:
            food = Food.query.filter_by(id=id).first()
            food.carbo = carbo
            food.measure = Measure(measure)
            food.name = name
            food.description = description
            food.quantity = quantity
            db.session.add(food)
            db.session.commit()

            response = {
                "id": food.id,
            }
            return {"message": "Alimento atualizado.", "data": response}, 200
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500

    @userAuthorization
    def delete(self, id):
        try:
            publication = Food.query.filter_by(id=id).first()
            db.session.delete(publication)
            db.session.commit()

            return {"message": "Alimento excluído."}, 200
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500


@api.route('/food-by-id/<id>')
class FoodByIdRoute(Resource):
    
    def get(self, id):
        try:
            food = Food.query.filter_by(id=id).first()
            if food == None:
                return {"error": "Alimento não encontrado."}, 400

            user = User.query.filter_by(id=food.author).first()

            response = {
                "id": food.id,
                "name": food.name,
                "description": food.description,
                "carbo": float(food.carbo),
                "quantity": None if not food.quantity else float(food.quantity),
                "measure": None if not food.measure else Measure(food.measure).value,
                "measureQuantity": None if not food.measureQuantity else int(food.measureQuantity),
                "user": {
                    "id": user.id,
                    "name": user.username
                }
            }

            return {"message": "Publication retrieved.", "data": response}, 200
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500


@api.route('/food-list')
class FoodListRoute(Resource):

    @userAuthorization
    def get(self):
        searchQuery = request.args.get('search')
        limit = 10
        page = 0

        try:
            page = int(request.args.get('page')) * 10
        except:
            return {"error": "Page not informed correctly."}, 400
        try:
            food = []
            if searchQuery:
                food = Food.query.filter(or_(Food.description.ilike("%"+searchQuery.lower()+"%"), Food.name.ilike("%"+searchQuery.lower()+"%"))).limit(limit).offset(page).all()
            else:
                food = Food.query.limit(limit).offset(page).all()
            
            if len(food) == 0:
                return None, 204

            def formatPublication(food):
                user = User.query.filter_by(id=food.author).first()
                return {
                "id": food.id,
                "name": food.name,
                "description": food.description,
                "carbo": float(food.carbo),
                "quantity": None if not food.quantity else float(food.quantity),
                "measure": None if not food.measure else Measure(food.measure).value,
                "measureQuantity": None if not food.measureQuantity else int(food.measureQuantity),
                "user": {
                    "id": user.id,
                    "name": user.username
                }
            }
            responseArray = list(map(formatPublication, food))

            return {"message": "Alimentos achados.", "data": responseArray}, 200

        except Exception as err:
            print(str(err))
            return {"error": 'Error connecting to database. Try again later.'}, 500