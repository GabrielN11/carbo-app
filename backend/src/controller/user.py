from flask import request
from flask_restx import Resource

from src.utils.authorization import userAuthorization
from env import JWT_KEY
import jwt


from src.server.instance import api, db
from src.models.user import User


@api.route('/user/<id>')
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

   @userAuthorization
   def put(self, id):
        username = None
        try:
            username = api.payload['username']
        except:
            return {"error": "Nome inválido."}, 400
        
        userId = jwt.decode(request.headers.get('Authorization').split()[1], JWT_KEY, algorithms="HS256")['id']

        print(userId, id)

        if int(id) != int(userId):
            return {"error": "Não autorizado."}, 400

        try:
            user = User.query.filter_by(id=id).first()

            if user.username == username:
                return {"error": "Não houve mudanças no nome de usuário."}, 400

            user.username = username

            db.session.add(user)
            db.session.commit()

            return {"message": "Nome de usuário alterado."}, 200
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500
    