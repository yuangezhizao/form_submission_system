from flask import Flask
from main.blueprints.todos import todos_bp
from main.plugins.extensions import db, csrf


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    app.config['SECRET_KEY'] = 'VG0^XPSf%hScY5TpS1#9lkQrTr@uBT8C'
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    csrf.init_app(app)


def register_blueprints(app):
    app.register_blueprint(todos_bp)
