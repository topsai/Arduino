#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import json
from channels import Group, Channel
import redis
import logging

all_device = {}


def ws_connect(message):
    print('ws_connect')
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True
        })
    })


def ws_disconnect(message):
    print('ws_disconnect')
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('users').discard(message.reply_channel)


def user_connect(message):
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




def user_disconnect(message):
    text = message.content.get('text')
    # print(message.content.reply_channel)


def user_receive(message):
    print('收到信息：%s ' % (message.content))
    text = message.content.get('text')
    data = json.loads(text)
    if data.get('device'):
        print('设备上线', data.get('device'), message.reply_channel.name)
        all_device[data.get('device')] = message.reply_channel.name


def send_invite(message):
    print('send message')
    print(all_device)
    Channel(all_device.get('smarthome')).send({'text': 'light on'})
