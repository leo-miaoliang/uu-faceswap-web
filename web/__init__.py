import os
from flask import Flask
from lib.config import config
from web.home import home as home_blueprint


def create_app(config_name='default'):
    app = Flask(__name__)
    conf = config[config_name]
    app.config.from_object(conf)
    app.register_blueprint(home_blueprint)
    return app

