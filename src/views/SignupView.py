  
import time
import datetime

from flask import Blueprint, Response, json
from flask import request, session
from src.models import UserModel, UserSchema, db
from src.utilities.CustomResponse import custom_response

signup_api = Blueprint('signup_api', __name__)
user_schema = UserSchema()

@signup_api.route('/', methods=['POST'])
def signup():
    dict_body=request.get_json()
    user_dict={}
    user_dict['name']=dict_body['name']
    user_dict['email']=dict_body['email']
    user_dict['password']=dict_body['password']
    user_dict['username']=dict_body['username']
    user_dict['phone_no']=dict_body['phone_no']
    user_dict['address']=dict_body['address']
    exist=UserModel.getcheck(dict_body['username'])
    if exist:
        return custom_response("Username already exists. Please use another one",400)
    data,err=user_schema.load(dict_body)
    if err:
        return custom_response("Error",400)
    user=UserModel(data)
    user.save()
    return custom_response("Success",200)
    

