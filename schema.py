from Models.seller import LendInfo
from marshmallow import fields
from db import db,ma


class LandSchema(ma.Schema):
    class Meta:
       model = LendInfo
       sqla_session = db.session
       
    id = fields.Number(dump_only=True)
    address = fields.String(dump_only=True)
    size = fields.String(dump_only=True)
