from flask import Flask


def create_app():
    app = Flask(__name__)

    from .home import home
    from .search import search

    app.register_blueprint(home, prefix="/")
    app.register_blueprint(search, prefix="/")

    return app
