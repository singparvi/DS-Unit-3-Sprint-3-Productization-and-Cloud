from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):

    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String, nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)  # keepts track of recent user tweet

    def __repr__(self):
        return "<User: {}".format(self.name)


class Tweet(DB.Model):

    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    vect = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
