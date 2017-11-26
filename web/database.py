"""BajtaHack database."""

import flask_sqlalchemy


def get_db(app):
  db = flask_sqlalchemy.SQLAlchemy()
  db.app = app
  db.init_app(app)
  return db
