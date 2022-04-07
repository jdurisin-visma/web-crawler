from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scrape.sqlite3'
    app.config['SECRET_KEY'] = "random string"

    db.init_app(app)

    return app
