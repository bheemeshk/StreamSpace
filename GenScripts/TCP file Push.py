__author__ = 'streamsadmin'


import socket
import sys

s = socket.socket()
s.connect(("localhost",23145))
f = open("/home/streamsadmin/workspace/AAPL.csv", "rb")
l = f.readline()
while(l):
    print(l)
    s.send(l)
    l = f.readline()
s.close()