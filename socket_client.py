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
    href = "ws://www.codefarmer.site/talk/"
    href1 = "ws://127.0.0.1:8000/talk/"
    ws = websocket.WebSocketApp(href,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                )
    ws.on_open = on_open
    ws.run_forever()
