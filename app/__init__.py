import os

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from .models import db
print(os.environ.get('DATABASE_URI'))

api = Api(app)

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.json.compact = False
  db.init_app(app)
  migrate = Migrate(app, db)


  from app import routes

  return app
