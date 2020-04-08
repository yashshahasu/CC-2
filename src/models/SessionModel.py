# src/models/BlogpostModel.py
from marshmallow import fields, Schema
from . import db
import datetime

class SessionModel(db.Model):
  """
  Session Model
  """

  __tablename__ = 'sessions'

  id = db.Column(db.Integer, primary_key=True)
  status_flag=db.Column(db.Boolean,nullable=False)
  start_time = db.Column(db.DateTime)
  end_time = db.Column(db.DateTime)
  last_entered_time=db.Column(db.DateTime)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

  def __init__(self, data):
    self.user_id = data.get('user_id')
    self.status_flag=data.get('status_flag')
    self.start_time = datetime.datetime.utcnow()
    self.end_time = datetime.datetime.utcnow()
    self.last_entered_time=datetime.datetime.utcnow()

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
class SessionSchema(Schema):
  """
  Session Schema
  """
  id = fields.Int(dump_only=True)
  status_flag = fields.Bool(required=True)
  start_time = fields.DateTime(required=True)
  end_time = fields.DateTime(required=True)
  last_entered_time = fields.DateTime(required=True)
  user_id = fields.Int(required=True)
