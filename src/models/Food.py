# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime
from . import db

class FoodModel(db.Model):
  """
  Food Model
  """

  # table name
  __tablename__ = 'food'

  id = db.Column(db.Integer, primary_key=True)
  user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
  comments=db.Column(db.String(128),nullable=False)
  price=db.Column(db.Integer,nullable=False)
  cuisine=db.Column(db.String(128),nullable=False)
  img_url=db.Column(db.String(128),nullable=False)
  quantity=db.Column(db.Integer,nullable=False)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """

    self.price = data.get('price')
    self.comments = data.get('comments')
    self.price = data.get('price')
    self.cuisine = data.get('cuisine')
    self.user_id=data.get('user_id')
    self.quantity=data.get('quantity')
    self.img_url=data.get('img_url')
    
  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def __repr(self):
    return '<id {}>'.format(self.id)


# add this class
class FoodSchema(Schema):
  """
  Food Schema
  """
  id = fields.Int(dump_only=True)
  price=fields.Int(required=True)
  user_id=fields.Int(required=True)
  comments=fields.Str(required=True)
  cuisine=fields.Str(required=True)
  quantity=fields.Int(required=True)
  img_url=fields.Str(required=True)
  