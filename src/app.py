#src/app.py

from flask import Flask
from .models import db
from .config import app_config
from .views.SignupView import signup_api as signup_blueprint
from .views.LoginView import login_api as login_blueprint

def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])
  db.init_app(app)
  app.register_blueprint(signup_blueprint,url_prefix='/signup')
  app.register_blueprint(login_blueprint,url_prefix="/login")

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Congratulations! Your first endpoint is workin'

  return app