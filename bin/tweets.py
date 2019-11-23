import fixpath
import socket

from src.services.Communication import send_data
from src.services.TwitterService import TwitterListener

s = socket.socket()
HOST = "127.0.0.1"
PORT = 5555
s.bind((HOST, PORT))

print("Listening on {} {}".format(HOST, PORT))
s.listen(5)
c,addr = s.accept()

send_data(c, TwitterListener, "flamengo")