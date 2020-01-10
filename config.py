# -*- coding: utf-8 -*-

from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY') or 'uma string randômica e gigante'
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())
    MONGODB_HOST = getenv('MONGODB_URI')


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    MONGODB_HOST = getenv('MONGODB_URI_TEST')


class TestingConfig(Config):
    TESTING = True
    FLASK_ENV = 'testing'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
