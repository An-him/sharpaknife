import os
from decouple import config
from datetime import timedelta


BASEDIR=os.path.dirname(os.path.realpath(__file__))

class Config():
    SECRET_KEY=config('SECRET_KEY', 'secret')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_SECRET_KEY=config('JWT_SECRET_KEY')




class DevConfig(Config):
    DEBUG=config('DEBUG',cast=bool)
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASEDIR,'dev.db')

class ProdConfig(Config):
    pass

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI='sqlite://' # In memory database
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True
    


config_dict={
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig
}