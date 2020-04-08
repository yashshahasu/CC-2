# src/models/BlogpostModel.py
from marshmallow import fields, Schema
from . import db
import datetime

class RequestModel(db.Model):
  """
  Request Model
  """

  __tablename__ = 'requests'

  id = db.Column(db.Integer, primary_key=True)
  status=db.Column(db.String(128),nullable=False)
  action=db.Column(db.String(128),nullable=False)
  role=db.Column(db.String(128),nullable=False)
  timestamp=datetime.datetime.utcnow()
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id'), nullable = False)

  def __init__(self, data):
    self.user_id = data.get('user_id')
    self.transaction_id=data.get('transaction_id')
    self.status=data.get('status')
    self.action=data.get('action')
    self.role=data.get('role')
    self.timestamp = datetime.datetime.utcnow()
    
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
class RequestSchema(Schema):
  """
  Request Schema
  """
  id = fields.Int(dump_only=True)
  action = fields.Str(required=True)
  status = fields.Str(required=True)
  role = fields.Str(required=True)
  timestamp = fields.DateTime(required=True)
  user_id = fields.Int(required=True)
  transaction_id = fields.Int(required=True)
