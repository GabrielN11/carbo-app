from flask import request
from flask_restx import Resource
from flask_mail import Message
from datetime import datetime, timedelta
import jwt
import random
import string

from src.server.instance import api, bcrypt, db, mail
from src.models.user import User
from src.utils.authorization import userAuthorization
from src.utils.email_template import generateValidationTemplate, generateRecoveryTemplate
from env import JWT_KEY, MAIL_ADDRESS

@api.route('/sign-up')
class SignUpRoute(Resource):
    def post(self):
        data = api.payload
        username = None
        password = None
        email = None
        try:
            username = data['username']
            password = data['password']
            email = data['email']
        except:
            return {"error": "Dados inválidos."}, 400

        if len(password) < 6:
            return {"error": "Senha é muito curta."}, 400

        if User.query.filter_by(username=username).first() != None:
            return {"error": "Nome de usuário já existe"}, 400

        if User.query.filter_by(email=email).first() != None:
            return {"error": "Email já está em uso"}, 400

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        
        try:
            user = User(username=username, password=hashed_pw, email=email)

            validationCode = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

            token = jwt.encode({"id": user.id, "code": validationCode, 'exp': datetime.utcnow() + timedelta(minutes=10)}, JWT_KEY, algorithm="HS256")

            msg = Message(
                'Confirmação CarboApp',
                sender = MAIL_ADDRESS,
                recipients = [email]
            )
            msg.html = generateValidationTemplate(username, validationCode)
            msg.body = f"""
            Olá @{username}! Para finalizar seu cadastro basta copiar o código abaixo e colar no site do CarboApp!

            Code: {validationCode}
            """
            mail.send(msg)

            user.validationtoken = token

            db.session.add(user)
            db.session.commit()

            data = {
                "id": user.id,
            }

            return {"message": "Usuário criado. Por favor cheque seu e-mail para confirmar o registro.", "data": data}, 201
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500

    def put(self):
        code = api.payload['code']
        id = api.payload['id']

        user = User.query.filter_by(id=id).first()

        if user.validationtoken == None:
            return {"error": "Esta conta já está ativada."}, 400

        if len(code) < 5:
            return {"error": "Código inválido."}, 400

        data = jwt.decode(user.validationtoken, JWT_KEY, algorithms="HS256")

        if data['code'] != code:
            return {"error": 'Código inválido.'}, 401


        try:
            user.active = True
            user.validationtoken = None
            db.session.add(user)
            db.session.commit()

            token = jwt.encode({"id": user.id, 'admin': user.admin, 'exp': datetime.utcnow() + timedelta(days=60)}, JWT_KEY, algorithm="HS256")
            
            data = {
                "id": user.id,
                "username": user.username,
                "is_admin": user.admin,
                "token": token
            }

            return {"message": "Conta validada com sucesso!.", "data": data}, 200
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500

        

@api.route('/sign-in')
class SignInRoute(Resource):

    @userAuthorization
    def get(self):
        userId = jwt.decode(request.headers.get('Authorization').split()[1], JWT_KEY, algorithms="HS256")['id']

        try:
            userData = User.query.filter_by(id=userId).first()
            if userData == None:
                return {"error": "User not found"}, 400

            user = {
                "id": userData.id,
                "username": userData.username,
                "email": userData.email,
                "admin": userData.admin,
                "token": request.headers.get('Authorization').split()[1]
            }
            return {"message": "User data retrieved", "data": user}, 200
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500

    def post(self):
        data = api.payload
        username = None
        password = None

        try:
            username = data['username']
            password = data['password']
        except:
            return {"error": "Missing data"}, 400

        userData = User.query.filter_by(username=username).first()

        if userData == None:
            return {"error": "Autenticação incorreta."}, 400

        if bcrypt.check_password_hash(userData.password, password):
            token = jwt.encode({"id": userData.id, 'admin': userData.admin, 'exp': datetime.utcnow() + timedelta(days=60)}, JWT_KEY, algorithm="HS256")

            if userData.active == False:
                validationCode = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

                token = jwt.encode({"id": userData.id, "code": validationCode, 'exp': datetime.utcnow() + timedelta(minutes=10)}, JWT_KEY, algorithm="HS256")

                msg = Message(
                    'Confirmação CarboApp',
                    sender = MAIL_ADDRESS,
                    recipients = [userData.email]
                )
                msg.html = generateValidationTemplate(username, validationCode)
                msg.body = f"""
                Olá @{username}! Para finalizar seu cadastro basta copiar o código abaixo e colar no site do CarboApp!

                Code: {validationCode}
                """
                mail.send(msg)
            
                data = {
                    "id": userData.id,
                }

                return {"message": "Validation sent.", "data": data}, 403
            user = {
                "id": userData.id,
                "username": username,
                "email": userData.email,
                "admin": userData.admin,
                "token": token
            }

            return {"message": "Successfully authenticated", "data": user}, 200
        else:
            return {"error": "Autenticação Inválida."}, 400

@api.route('/recovery')
@api.route('/recovery/<id>')
class RecoveryRoute(Resource):
    
    def post(self):
        email = api.payload['email']
        if email == None:
            return {"error": "Missing data."}, 400
        
        try:
            user = User.query.filter_by(email=email).first()
            if user == None:
                return {"error": "E-mail inválido."}, 400

            recoveryCode = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

            token = jwt.encode({"id": user.id, "code": recoveryCode, 'exp': datetime.utcnow() + timedelta(minutes=10)}, JWT_KEY, algorithm="HS256")
            msg = Message(
                'Recuperação CarboApp',
                sender = MAIL_ADDRESS,
                recipients = [user.email]
            )
            msg.html = generateRecoveryTemplate(user.username, recoveryCode)
            msg.body = f"""
            Olá @{user.username}! Para recuperar sua conta, insira o código abaixo no site do CarboApp.

            Código: {recoveryCode}
            """
            mail.send(msg)

            user.validationtoken = token
            db.session.add(user)
            db.session.commit()

            return {"message": f"Email de recuperção enviado para {email}!", "data": {id: user.id}}, 200
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500

    def get(self, id):
        code = request.args.get('code')

        user = User.query.filter_by(id=id).first()

        data = None
        try:
            data = jwt.decode(user.validationtoken, JWT_KEY, algorithms="HS256")
        except:
            return {"error": 'Autenticação incorreta.'}, 403

        if data == None or data['code'] != code:
            return {"error": 'Autenticação incorreta.'}, 403

        user.validationtoken = None

        db.session.add(user)
        db.session.commit()

        return {"message": "Autenticado.", "data": {"id": user.id}}, 200

    def put(self, id):
        password = api.payload['password']
        if len(password) < 6:
            return {"error": "Senha é muito curta."}, 400
        
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        try:
            user = User.query.filter_by(id=id).first()

            user.password = hashed_pw

            db.session.add(user)
            db.session.commit()

            return {"message": "Senha alterada."}, 200
        except Exception as err:
            print(str(err))
            return {"error": "Error connecting to database. Try again later."}, 500