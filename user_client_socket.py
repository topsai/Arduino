#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# 客户端 运行在arduino上游设备
# 负责与服务器通讯，并将服务器下发的消息解析发送给arduino


import websocket
import serial

ser = serial.Serial('/dev/ttyUSB0')


def opeate_arduino(device, status):
    # 操作设备，连接并操作设备，返回操作是否成功
    # TODO ing...
    ret = False
    import serial
    s = serial.Serial()
    s.write()
    return ret


def on_message(ws, message):
    device, status = message.split(',')
    print(device, status)
    if device == 'light':
        # 灯
        if status == 'open' or status == 'on':
            # turn on the linht
            ser.write('a')
        else:
            ser.write('b')


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    pass


if __name__ == "__main__":
    websocket.enableTrace(True)
    href = "wss://alexa.detaomedia.com/talk/"
    href1 = "ws://127.0.0.1:8000/talk/"
    ws = websocket.WebSocketApp(href,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                cookie='smarthome',  # 用于识别设备信息，不写无法连接
                                )
    ws.on_open = on_open
    ws.run_forever()
