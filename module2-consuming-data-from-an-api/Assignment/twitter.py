import tweepy
import os
from data_model import DB, User, Tweet
from dotenv import load_dotenv
import spacy
import en_core_web_sm

load_dotenv()
# twitter_api_key = os.environ['TWITTER_API_KEY']
# twitter_api_secret = os.environ['TWITTER_API_KEY_SECRET']
twitter_api_key = os.getenv('TWITTER_API_KEY')
twitter_api_secret = os.getenv('TWITTER_API_KEY_SECRET')
twitter_auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
twitter_api = tweepy.API(twitter_auth)

# nlp model
nlp = spacy.load('my_model')

def vectorize_tweet(tweet_text):
    return nlp(tweet_text).vector


def upsert_user(twitter_handle):
    try:
        twitter_user = twitter_api.get_user(twitter_handle)
        if User.query.get(twitter_user.id):
            db_user = User.query.get(twitter_user.id)
        else:
            db_user = User(id=twitter_user.id, name=twitter_handle)
        DB.session.add(db_user)

        user_tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode="extended")

        if user_tweets:
            db_user.newest_tweet_id = user_tweets[0].id

        for tweet in user_tweets:
            vectorized_tweet = vectorize_tweet(tweet.full_text)
            db_tweet = Tweet(id=tweet.id, text=tweet.full_text, vect=vectorized_tweet)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)
    except Exception as e:
        raise e
    else:
        DB.session.commit()
