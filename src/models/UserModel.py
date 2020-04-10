# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime
from . import db
from .Food import FoodSchema
from .Art import ArtSchema

class UserModel(db.Model):
  """
  User Model
  """

  # table name
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.Text, nullable=False)
  username = db.Column(db.String(128), nullable=False,unique=True)
  phone_no= db.Column(db.String(128),nullable=False)
  address=db.Column(db.String(128),nullable=False)
  food=db.relationship('FoodModel',backref='users',lazy=True)
  art=db.relationship('ArtModel',backref='users',lazy=True)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """

    self.name = data.get('name')
    self.email = data.get('email')
    self.password = data.get('password')
    self.username = data.get('username')
    self.phone_no=data.get('phone_no')
    self.address=data.get('address')
    
  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()
  
  def getcheck(username):
    return UserModel.query.filter_by(username=username).first()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def __repr(self):
    return '<id {}>'.format(self.id)


# add this class
class UserSchema(Schema):
  """
  User Schema
  """
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  email = fields.Str(required=True)
  password = fields.Str(required=True)
  username = fields.Str(required=True)
  phone_no = fields.Str(required=True)
  address=fields.Str(required=True)
  food=fields.Nested(FoodSchema,many=True)
  art=fields.Nested(ArtSchema,many=True)