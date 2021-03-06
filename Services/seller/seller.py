from dbm import dumb
from importlib.resources import Resource
from operator import add
from sys import maxsize
from Models.buyer import Buyer, BuyerBudding
from Models.seller import Seller, LendInfo,  PropertyQuote, SellerInfo
from flask_restful import Resource, request
from flask import abort, jsonify, make_response
from db import db
from passlib.apps import custom_app_context as pwd_context

from schema import LandSchema, BuddingSchema
from sqlalchemy import func


# seller register view

def json_token():
    pass
class sellerRegister(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        if email is None or password is None:
            # abort(400)
            return jsonify({'error': 'Please enter email or password'})
        if Seller.query.filter_by(email=email).first() is not None:
            # abort(400)
            return jsonify({'error': 'Email already exists, Enter different email.'})
        user = Seller(email=email)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'email': user.email, 'status': 'successfully registered'})


# seller login view
class sellerLogin(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')

        user = Seller.query.filter_by(email=email).first()

        passs = (pwd_context.verify(password, user.password_hash))
        
        if passs == True:

            return jsonify({'User': user.email, 'status': 'successfully logged In'})
        else:
            return jsonify({'status': 'Incorrect email or password'})


# land information view
class lendInformation(Resource):
    def post(self):
        address = request.json['address']
        size = request.json['size']

        land = LendInfo(address=address, size=size)
        db.session.add(land)
        db.session.commit()
        return jsonify({"status": "successfully registered"})

# land quotes view


class PropertyQuoteView(Resource):
    def post(self):
        property_id = request.json['property_id']
        quote = 100000

        property = PropertyQuote(property_id=property_id, quote=quote)
        db.session.add(property)
        db.session.commit()
        return jsonify({"status": "successfully registered"})


# seller Information view
class SellerInfoView(Resource):
    def post(self):
        name = request.json['name']
        email = request.json['email']
        mobile = request.json['mobile']

        seller = SellerInfo(name=name, email=email, mobile=mobile)
        db.session.add(seller)
        db.session.commit()
        return jsonify({"status": "Successfully registered"})


# get land list
class LandListView(Resource):
    def get(self):
        land = LendInfo.query.all()
        landSchema = LandSchema(many=True)
        landList = landSchema.dump(land)

        return jsonify({"land list": landList})


# highest bid
class HighestBidView(Resource):

    def get(self):

        # bid = BuyerBudding.query.filter_by()

        max_bid = db.session.query(func.max(BuyerBudding.bid)).scalar()
        bid = db.session.query(BuyerBudding).filter(
            BuyerBudding.bid == max_bid).all()

        buddingSchema = BuddingSchema(many=True)
        buddingList = buddingSchema.dump(bid)

        return jsonify({"Bid list": buddingList})
