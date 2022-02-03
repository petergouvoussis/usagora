import os

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigSetup:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', None)
