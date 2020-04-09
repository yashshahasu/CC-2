# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime
from . import db

class ArtModel(db.Model):
  """
  Art Model
  """

  # table name
  __tablename__ = 'art'

  id = db.Column(db.Integer, primary_key=True)
  type_of_art=db.Column(db.String(128),nullable=False)
  img_url=db.Column(db.String(128),nullable=False)
  price=db.Column(db.Integer,nullable=False)
  user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
  size_of_art=db.Column(db.Integer,nullable=False)
  weight=db.Column(db.Integer,nullable=False)
  comments=db.Column(db.String(128),nullable=False)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """

    self.type_of_art = data.get('type_of_art')
    self.user_id=data.get('user_id')
    self.img_url = data.get('img_url')
    self.price = data.get('price')
    self.size_of_art = data.get('size_of_art')
    self.weight=data.get('weight')
    self.comments=data.get('comments')
    
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
class ArtSchema(Schema):
  """
  Art Schema
  """
  id = fields.Int(dump_only=True)
  user_id=fields.Int(required=True)
  comments=fields.Str(required=True)
  type_of_art=fields.Str(required=True)
  img_url=fields.Str(required=True)
  price=fields.Int(required=True)
  size_of_art=fields.Str(required=True)
  weight=fields.Int(required=True)