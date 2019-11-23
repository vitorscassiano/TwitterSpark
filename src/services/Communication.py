import os
import config.settings

from tweepy import OAuthHandler, Stream

def send_data(csocket, TwitterListener, keyword):
  CONSUMER_KEY = os.getenv("CONSUMER_KEY")
  CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
  ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
  ACCESS_SECRET = os.getenv("ACCESS_SECRET")

  auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

  if(type(keyword) == str):
    words = [keyword]
  elif(type(keyword) == list):
    words = keywords
  else:
    raise Exception("Type does not found!")

  twitter_stream = Stream(auth=auth, listener=TwitterListener(csocket))
  twitter_stream.filter(track=words)