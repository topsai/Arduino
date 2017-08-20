#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import websocket
import _thread as thread
import time


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")

import json
def on_open(ws):
    print(dir(ws))
    ws.send(json.dumps({"device": 'smarthome'}))
    # def run(*args):
    #     for i in range(3):
    #         time.sleep(1)
    #         ws.send("Hello %d" % i)
    #     time.sleep(1)
    #     ws.close()
    #     print("thread terminating...")
    #
    # thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://www.codefarmer.site:443/talk/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                )
    ws.on_open = on_open
    ws.run_forever()


# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_callback', '_get_close_args', '_send_ping', 'close', 'cookie', 'get_mask_key', 'header', 'keep_running', 'last_ping_tm', 'last_pong_tm', 'mmm', 'on_close', 'on_cont_message', 'on_data', 'on_error', 'on_message', 'on_open', 'on_ping', 'on_pong', 'run_forever', 'send', 'sock', 'subprotocols', 'url']
