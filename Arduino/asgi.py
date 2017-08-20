#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import os
from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Arduino.settings")

channel_layer = get_channel_layer()
