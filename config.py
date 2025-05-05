import os
import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Config() :
    SQLALCHEMY_DATABASE_URI = 'sqlite:///banco.db'

