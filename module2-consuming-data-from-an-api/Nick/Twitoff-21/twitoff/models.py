"""SQLAlchemy models and utility functions for Twitter Application"""

from flask_sqlalchemy import SQLAlchemy

# instances of SQLAlchemy class
DB = SQLAlchemy()


class User(DB.Model):
    """This is the way you create a table using SQLAlchemy.
    Twitter User table that will correspond to tweets - SQLAlchemy syntax"""
    id = DB.Column(DB.BigInteger, primary_key=True)  # This is a way you make ID column in a table using SQLAlchemy
    name = DB.Column(DB.String, nullable=False)  # Name column, have to have a name in the table

    def __repr__(self):
        return "<User: {}>".format(self.name)


class Tweet(DB.Model):
    """Tweet text data - associated with Users Table"""
    id = DB.Column(DB.BigInteger, primary_key=True)  # id column (primary key)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"),
                        nullable=False)  # Foreign Key, (secondary key) comes from another table and the value
    # must be present in the primary table to use the value in Foreign Key
    # create a relationship now
    user = DB.relationship('User', backref=DB.backref('tweets',
                                                      lazy=True))  # This relationship is really a join. Whenever we reference one we reference the other. Basically this is doing is it joins them. Backref User tweets and associate it with the Foregin Key.

    def __repr__(self):
        return f"<Tweet: {self.text}>"
