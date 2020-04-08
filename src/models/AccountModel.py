# src/models/BlogpostModel.py
from marshmallow import fields, Schema
from . import db
import datetime

class AccountModel(db.Model):
  """
  Account Model
  """

  __tablename__ = 'accounts'

  id = db.Column(db.Integer, primary_key=True)
  account_no = db.Column(db.Integer, nullable=False)
  account_type= db.Column(db.String(128),nullable=False)
  logs=db.Column(db.String(128),nullable=False)
  timestamp = db.Column(db.DateTime)
  amount=db.Column(db.Integer,nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  

  def __init__(self, data):
    self.id = data.get('id')
    self.user_id = data.get('user_id')
    self.account_no = data.get('account_no')
    self.account_type = data.get('account_type')
    self.logs = data.get('logs')

    self.timestamp = datetime.datetime.utcnow()
    self.amount= data.get('amount')
    
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

  def __repr__(self):
    return '<id {}>'.format(self.id)

# add this class
class AccountSchema(Schema):
  """
  Account Schema
  """
  id = fields.Int(dump_only=True)
  account_no = fields.Int(required=True)
  amount = fields.Int(required=True)
  account_type = fields.Str(required=True)
  logs = fields.Str(required=True)
  timestamp = fields.DateTime(required=True)
  user_id = fields.Int(required=True)
