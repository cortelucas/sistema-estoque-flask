import os
import random
import string


class Config(object):
    CSRF_ENABLED = True
    SECRET = "61926647da9b58e9f996ba2557da19500aec84cad4bc358e137ee2ffb8ac4d87"
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://fatec@localhost:3306/sistema_estoque'


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'


class ProductionConfig(Config):
    DEBUG = False
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'


app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')
