import time
import datetime

from flask import Blueprint, Response, json
from flask import request, session
from src.utilities.CustomResponse import custom_response
from ..models import UserModel,db,UserSchema

login_api = Blueprint('login', __name__)
user_schema = UserSchema()

@login_api.route('/', methods=['POST'])
def login():
    dict=request.get_json()
    exist=UserModel.getuser(dict['username'],dict['password'])
    if not exist:
        message="User does not exists. Please Sign up"
        return custom_response(message,403)
    else:
        return custom_response("Success",200)
        
        
