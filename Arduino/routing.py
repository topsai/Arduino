#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from channels.routing import route, include

# from StudentManagement.comsumers import ws_connect, ws_disconnect, ws_receive
from alexa_channel.consumers import ws_connect, ws_disconnect, user_connect, user_disconnect, user_receive

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]
user_routing = [
    route('websocket.connect', user_connect),
    route('websocket.disconnect', user_disconnect),
    route('websocket.receive', user_receive)
]
routing = [
    include(channel_routing, path=r"^/users"),
    # 同django可以使用include代替route指定路由组
    include(user_routing, path=r"^/talk"),
    # 同django可以使用include代替route指定路由组
    # include(http_routing),
]

# http_routing = [
#     route("http.request", poll_consumer, path=r"^/poll/$", method=r"^POST$"),
# ]
#
# chat_routing = [
#     route("websocket.connect", chat_connect, path=r"^/(?P<room>[a-zA-Z0-9_]+)/$"), #path同dajngo的path可以使用正则表达式取参数
#     route("websocket.disconnect", chat_disconnect),
# ]
#
# routing = [
#     include(chat_routing, path=r"^/chat"),  #同django可以使用include代替route指定路由组
#     include(http_routing),
# ]