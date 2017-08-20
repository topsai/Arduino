#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import socket

sk = socket.socket()
sk.bind(("0.0.0.0", 64000))
sk.listen(1)
