# -*- coding: utf-8 -*-
from flask import Flask
from config import config

from .api import configure_api
from .db import db


def create_app(config_name):
    app = Flask('api-gestão')
    app.config.from_object(config[config_name])

    # Configure MongoEngine
    db.init_app(app)

    # executa a chamada da função de configuração
    configure_api(app)

    return app
