from flask import Flask
from app.model.book import db


def create_app():
    app = Flask(__name__)
    #app.config.from_object('app.secure')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+cymysql://root:root@127.0.0.1:3306/fisher'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    print("create app")
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web
    from app.web.user import web
    app.register_blueprint(web)
