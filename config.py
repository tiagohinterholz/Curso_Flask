DEBUG = True

USERNAME = 'tiago'
PASSWORD = 'tiago'
SERVER = 'localhost'
DB = 'api_flask'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "aplicacao_flask"