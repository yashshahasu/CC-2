# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime
from . import db
from .TransactionModel import TransactionSchema
from .SessionModel import SessionSchema
from .RequestModel import RequestSchema
from .AccountModel import AccountSchema

class UserModel(db.Model):
  """
  User Model
  """

  # table name
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(128), nullable=False)
  last_name = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.Text, nullable=False)
  username = db.Column(db.String(128), nullable=False)
  role = db.Column(db.String(128), nullable=False)
  is_active = db.Column(db.Boolean, default=False)
  last_login = db.Column(db.DateTime)
  phone_no= db.Column(db.String(128),nullable=False)
  transactions = db.relationship('TransactionModel', backref='users', lazy=True)
  sessions = db.relationship('SessionModel', backref='users', lazy=True)
  requests = db.relationship('RequestModel', backref='users', lazy=True)
  accounts = db.relationship('AccountModel', backref='users', lazy=True)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """

    self.first_name = data.get('first_name')
    self.last_name = data.get('last_name')
    self.email = data.get('email')
    self.password = data.get('password')
    self.username = data.get('username')
    self.role = data.get('role')
    self.is_active = data.get('is_active')
    self.phone_no = data.get('phone_no')
    self.last_login = datetime.datetime.utcnow()
    
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

  @staticmethod
  def get_all_users():
    return User_Table.query.all()

  @staticmethod
  def get_one_user(id):
    return User_Table.query.get(id)

  
  def __repr(self):
    return '<id {}>'.format(self.id)


# add this class
class UserSchema(Schema):
  """
  User Schema
  """
  id = fields.Int(dump_only=True)
  first_name = fields.Str(required=True)
  last_name = fields.Str(required=True)
  email = fields.Str(required=True)
  password = fields.Str(required=True)
  username = fields.Str(required=True)
  role = fields.Str(required=True)
  is_active = fields.Bool(required=True)
  last_login = fields.DateTime(required=True)
  phone_no = fields.Str(required=True)
  transactions = fields.Nested(TransactionSchema, many=True)
  sessions = fields.Nested(SessionSchema, many=True)
  requests = fields.Nested(RequestSchema, many=True)
  accounts = fields.Nested(RequestSchema, many=True)
