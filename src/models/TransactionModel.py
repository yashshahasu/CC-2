from marshmallow import fields, Schema
import datetime
from . import db
from .RequestModel import RequestSchema

class TransactionModel(db.Model):
  """
  Transaction Model
  """

  # table name
  __tablename__ = 'transactions'

  id = db.Column(db.Integer, primary_key=True)
  transaction_id = db.Column(db.Integer, nullable=False)
  status = db.Column(db.String(128), nullable=True)
  amount=db.Column(db.Integer,nullable=False)
  sender_account_no=db.Column(db.Integer,nullable=False)
  receiver_account_no=db.Column(db.Integer,nullable=False)
  timestamp = db.Column(db.DateTime)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  requests = db.relationship('RequestModel', backref='users', lazy=True)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """

    self.user_id = data.get('user_id')
    self.transaction_id = data.get('transaction_id')
    self.timestamp = datetime.datetime.utcnow()
    self.status = data.get('status')
    self.amount = data.get('amount')
    self.sender_account_no = data.get('sender_account_no')
    self.receiver_account_no = data.get('receiver_account_no')

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
class TransactionSchema(Schema):
  """
  Transaction Schema
  """
  id = fields.Int(dump_only=True)
  transaction_id = fields.Int(required=True)
  status = fields.Str(required=True)
  amount = fields.Int(required=True)
  sender_account_no = fields.Int(required=True)
  receiver_account_no = fields.Int(required=True)
  cover_image_url = fields.Str(required=True)
  timestamp = fields.DateTime(dump_only=True)
  user_id = fields.Int(required=True)
  requests = fields.Nested(RequestSchema, many=True)