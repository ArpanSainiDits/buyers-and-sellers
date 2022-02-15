from lib2to3.pgen2 import token
from Models.buyer import Buyer, BuyerBudding
from flask import abort, jsonify, current_app
from db import db, app
from passlib.apps import custom_app_context as pwd_context
from flask_restful import Resource, request
import jwt
from datetime import datetime,  timedelta
from functools import wraps




def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        
        if not token:
            return jsonify({'message':'Token is missing!'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid!'})
        return f(*args, **kwargs)
        
    return decorated

# buyer register view
class buyerRegister(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        if email is None or password is None:
            # abort(400)
            return jsonify({'error': 'Please enter email or password'})
        if Buyer.query.filter_by(email=email).first() is not None:
            # abort(400)
            return jsonify({'error': 'Email already exists, Enter different email.'})
        user = Buyer(email=email)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'email': user.email, 'status': 'successfully registered'})


# buyer login view

class buyerLogin(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        user = Buyer.query.filter_by(email=email).first()
        passs = (pwd_context.verify(password, user.password_hash))
        if passs == True:
            token = jwt.encode({
                'sub': user.email,
                'exp': datetime.utcnow() + timedelta(minutes=30)},
                current_app.config['SECRET_KEY'])
            return jsonify({'status': 'successfully logged In','token': token.decode('UTF-8')})
        else:
            return jsonify({'status': 'Incorrect email or password'})


# Buyer bid
class BuyerBuddingView(Resource):
    def post(self):
        property_id = request.json['property_id']
        bid = request.json['bid']

        property = BuyerBudding(property_id=property_id, bid=bid)
        db.session.add(property)
        db.session.commit()
        return jsonify({"status": "successfully registered"})
