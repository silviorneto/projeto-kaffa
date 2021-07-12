from environs import Env
from flask import Flask


from app import views
from app.configs import commands, database, migrations, jwt

env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["JWT_SECRET_KEY"] = env("SECRET_KEY")

    # commands.init_app(app)
    database.init_app(app)
    migrations.init_app(app)
    views.init_app(app)
    jwt.init_app(app)

    return app
