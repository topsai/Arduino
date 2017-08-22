# app介绍
## alexa_channels

通过websocket实现和客户端实时通讯
用户设备通过 user_client.py 程序接入服务端 实现websocket

## django_alexa

接收alexa发送的数据，解析为相应的命令，发送到对应的alexa_channels中