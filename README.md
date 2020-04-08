# SBS

Requires:
Python3.x
PostgreSQL
virtualenv

Create virtualenv:
brew install pipenv

Activate virtualenv:
pipenv --three

Open shell of virual environment:
pipenv shell

Install all dependencies:
pip install -r requirements.txt or pipenv install flask flask-sqlalchemy psycopg2 flask-migrate flask-script marshmallow flask-bcrypt pyjwt

Migrations:
python manage.py db init
python manage.py db migrate

Run:
python run.py
