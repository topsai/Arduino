#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import os, sys
# sys.path.append('/usr/local/virtunlenvs/Arduino/Arduino')
sys.path.append('/usr/local/virtunlenvs/Arduino')
# sys.path.append('/home/banjer') # this line solved it
sys.executable = '/usr/local/virtunlenvs/Arduino/virtual_evn/bin/python'


from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Arduino.settings")

channel_layer = get_channel_layer()
