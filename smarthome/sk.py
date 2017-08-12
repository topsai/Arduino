#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import socket

sk = socket.socket()
sk.bind(('0.0.0.0', 443))
sk.listen(1)
conn, address = sk.accept()
print('IP:{}, PORT:{}'.format(*address))
conn.sendall('welcome'.encode())
while True:
    user_input = conn.recv(8096).decode()
    print(user_input)
