from db import db
from passlib.apps import custom_app_context as pwd_context


class Buyer(db.Model):
    __tablename__ = 'buyer'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(52), index=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)


class BuyerBudding(db.Model):
    __tablename__ = 'buyerBudding'
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer)
    bid = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)


db.create_all()
