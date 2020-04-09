#src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# initialize our db
db = SQLAlchemy()

from .UserModel import UserModel, UserSchema
from .Art import  ArtModel,ArtSchema
from .Food import FoodModel,FoodSchema