from os import getenv
from flask import Flask, render_template
from models import DB, User
from twitter import add_or_update_user


def create_app():
    """Create Flask Application"""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)

    @app.route("/")
    def root():
        """At end point '/'"""
        return render_template("base.html", title="Home", users=User.query.all())

    # @app.route('/update')
    # def update():
    #     """Updates each user"""
    #     update_all_users()
    #     return render_template("base.html", title="Users Updated!", users=User.query.all())

    @app.route("/reset")
    def reset():
        """reset DB using drop_all()"""
        DB.drop_all()
        DB.create_all()
        add_or_update_user("elonmusk")
        add_or_update_user("AOC")
        return render_template("base.html", title="RESET", users=User.query.all())

    return app


#
# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     DB.init_app(app)
#
#     @app.route('/')
#     def landing():
#         # DB.drop_all()
#         DB.create_all()
#         app_user = User(id=1, name='app_user')
#         DB.session.add(app_user)
#         DB.session.commit()
#         return render_template('base.html',
#                                title='Home',
#                                users=User.query.all())
#
#     @app.route('/add_user')
#     def root():
#         # DB.drop_all()
#         DB.create_all()
#         app_user = User(id=1, name='app_user')
#         DB.session.add(app_user)
#         DB.session.commit()
#
#         return render_template('base.html',
#                                title='Home',
#                                users=User.query.all())
#
#         # return "text"
#         # PS muse: when you are using Title = Home you are using Jinja2
#
#     return app

    # with app.app_context():
    #     user = db.User(...)
    #     db.session.add(user)
    #     db.session.commit()

# with create_app() as app:
#     add_or_update_user('nasa')
#
# if __name__ == "__main__":
#     create_app().run(host='0.0.0.0', port=8888)
