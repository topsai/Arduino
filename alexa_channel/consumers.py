#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from channels import Group, Channel

all_device = {}


def user_connect(message):
    print('connect', message)
    # 连接认证，没有cookie信息拒绝链接
    accept = False
    cookie_value = None

    for i in message.content['headers']:
        if i[0] == b'cookie' and i[1]:
            accept = True
            cookie_value = i[1]
    message.reply_channel.send({'accept': accept})
    if accept:
        all_device[cookie_value.decode()] = message.reply_channel.name
        print('设备上线', cookie_value.decode(), message.reply_channel.name)


def user_disconnect(message):
    print(message.content)
    device = None
    for k, v in all_device.items():
        if v == message.reply_channel.name:
            device = k
            del all_device[k]
            break
    print('设备下线', device, message.reply_channel.name)


def user_receive(message):
    print('收到信息：%s ' % (message.content))


def send_invite(message):
    print('send message')
    print(all_device)
    Channel(all_device.get('smarthome')).send({'text': 'light on'})
