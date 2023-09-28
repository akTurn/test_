import os
import secrets
import string

basedir = os.path.abspath(os.path.dirname(__file__))

def generate_secret_key(length=24):
    characters = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(characters) for _ in range(length))
    return secret_key

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:test123@localhost:3306/python_db'
    JWT_SECRET = generate_secret_key()


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', None)
    JWT_SECRET = os.environ.get('JWT_SECRET', None)


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:////{os.path.join(basedir, "test.sqlite")}'