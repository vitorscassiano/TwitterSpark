import json
import os

from tweepy import StreamListener 

class TwitterListener(StreamListener):
  def __init__(self, csocket):
    self.client_socket = csocket

  def on_connect(self):
    print("Connected!")

  def on_data(self, data):
    try:
      message = json.loads(data)
      msg = (message["text"] + '\n').encode("utf-8")
      print(msg)
      self.client_socket.send(msg)
      # self.client_socket.send(message["text"].encode("utf-8"))
    except BaseException as e:
      print("Error:", e)

    return True

  def on_error(self, status_code):
    print("Error: {}".format(status_code))

  def on_disconnect(self, notice):
    print("Disconnected: {}".format(notice))
