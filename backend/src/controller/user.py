from flask import request
from flask_restx import Resource

from src.server.instance import api
from src.models.user import User


@api.route('/user/:id')
class UserRoute(Resource):
   def get(self, id):
        try:
            userData = User.query.filter_by(id=id).first()
            if userData == None:
                return {"error": "User not found"}, 400

            user = {
                "id": userData.id,
                "username": userData.username
            }
            return {"message": "User data retrieved", "data": user}, 200
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500