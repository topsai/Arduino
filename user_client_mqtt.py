#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")
    # client.subscribe("user/{}".format(user_id))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    print(msg.payload.decode())
    client.user_data_set('asfasf')


def on_disconnect(*args, **kwargs):
    print('dis')
    print(args)
    print(kwargs)




user_id = '666'
client = mqtt.Client(client_id=user_id, clean_session=False)
client.on_connect = on_connect
client.on_message = on_message
client.disconnect = on_disconnect
client.username_pw_set('username', 'password')

client.connect("alexa.detaomedia.com")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
