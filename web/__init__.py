"""Base web app for BajtaHack."""

from flask import Flask

from web import views
from web import database
from web import models


DATABASE_URI = 'sqlite:////tmp/sqlalchemy_example.db'


def create_app():
    """Create b"""
    app_ = Flask(__name__)
    app_.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app_.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    views.init_views(app_)
    return app_


app = create_app()
db = database.get_db(app)
models.init_db(db)


__all__ = [
    'app',
    'db',
]
