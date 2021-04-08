1. Add volume to an existing container 

You can commit your existing container (that is create a new image from container’s changes) and then run it with your new mounts.

Example:

```$ docker ps  -a
CONTAINER ID        IMAGE                 COMMAND                  CREATED              STATUS                          PORTS               NAMES
    5a8f89adeead        ubuntu:14.04          "/bin/bash"              About a minute ago   Exited (0) About a minute ago                       agitated_newton

$ docker commit 5a8f89adeead newimagename

$ docker run -ti -v "$PWD/somedir":/somedir newimagename /bin/bash.

```

## Flask

1. sudo pip install pipenv

2. pipenv install flask jinja2 flask-sqlalchemy # this must be done in the base repo

3. FLASK_APP=twitoff flask run # run the flask webserver

4.  FLASK_APP="twittoff' flask shell

5. from twitoff.models import User

6. flask shell

7. source venv/bin/activate # for activating the venv shell

8.FLASKSQLalchemy commands 
DB.drop_all()
DB.create_all()
DB.session.add()
DB.session.commit()
Tweet.query.all()

from data_model import DB, Tweet, User
DB.drop_all()
DB.create_all()
app_user = User(id=1, name='name')
DB.session.add(app_user)
DB.session.commit()
print(User.query.all())

8. Spacy NLP module



