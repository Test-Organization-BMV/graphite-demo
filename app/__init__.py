from flask import Flask


def create_app():
    app = Flask(__name__)
    register_blueprints(app=app)
    return app


def register_blueprints(app: Flask):
    from app.routes.main import bp as main_blueprint
    app.register_blueprint(main_blueprint)
