#!/usr/bin/env python

import socket
def message():
  message = raw_input("Give command 'key_in -get { key_number }' or 'key_in -set { key_number }': ")
  return message

class client():

  def __init__(self):
    self.adres = ('127.0.0.1', 6500)
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  def connection(self, message):
    self.sock.connect(self.adres)
    self.sock.sendall(str(message))
    data = self.sock.recv(16)
    print data
    self.connection_close()

  def connection_close(self):
    print "cos"
    self.sock.close()

try:
  start = client()
  start.connection(message())
except:
  raise
  print 'error'