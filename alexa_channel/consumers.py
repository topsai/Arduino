#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import json
from channels import Group, channel
import redis
from channels.auth import channel_session_user, channel_session_user_from_http, channel_session

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
    print('user_connect')
    message.reply_channel.send({'accept': True})


def user_disconnect(message):
    print('user_disconnect')
    print(message.reply_channel)


def user_receive(message):
    print('收到信息：%s ' % (message.content))
    text = message.content.get('text')
    data = json.loads(text)
    if data.get('device'):
        print('设备上线', data.get('device'))
        all_device[data.get('device')] = message.reply_channel
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    r.set('all_device', all_device)  # 添加

