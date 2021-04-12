"""Main app/routing file for Twitoff"""

from flask import Flask, render_template
from .models import DB, User


# create application
def create_app():
    """Creating and configuring an instance of the Flask application"""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)  # initialize the DB with our application. DB is just an instance of the SQLalchemy class.

    # TODO - make rest of application
    @app.route('/')  # decorators - Python. Map a URL to a specific function.
    # editing functions without functions.
    # decorator already created by flask. Flask sees this and see the logic to app route decorator
    # we are setting up the base url. Where this function will be executed.
    # decorator to direct routes
    def root():
        return render_template('base.html', title="home", users=User.query.all())

    return app
