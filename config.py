import os

DEBUG = True

USERNAME = 'tiago'
PASSWORD = 'tiago'
SERVER = 'localhost'
DB = 'api_flask'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.getenv('SECRET_KEY', 'aplicacao flask')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'apicacao flask')