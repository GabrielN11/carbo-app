from functools import wraps
from flask import request
import jwt

from env import JWT_KEY
from src.server.instance import server

api = server.api

def userAuthorization(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authorization = request.headers.get('Authorization')
        if not authorization:
            return {"error": 'Não autorizado.'}, 401

        token = authorization.split()[1]
        try:
            data = jwt.decode(token, JWT_KEY, algorithms="HS256")  
            if not data and data['id']:
                return {"error": 'Não autorizado.'}, 401
        except Exception as err:
            return {"error": 'Não autorizado.'}, 401

        return f(*args, **kwargs)

    return decorated