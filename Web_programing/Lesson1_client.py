#!/usr/bin/env python

import socket
con_adres = ('0.0.0.0', 6500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect(con_adres)
sock.sendall("du")
conn.close()