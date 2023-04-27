from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)


    app.config['SECRET_KEY'] = '1234'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/film'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)


    migrate = Migrate(app, db)


    from app.films import films_blueprint
    app.register_blueprint(films_blueprint, url_prefix='/films')


    return app
