#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import requests

# data = {
#     "session": {
#         "new": False,
#         "sessionId": "SessionId.a96fc272-1346-495f-8789-aac51a51978c",
#         "application": {
#             "applicationId": "amzn1.ask.skill.c916f111-fe9e-4b9a-9fe4-33ea7b30eeb9"
#         },
#         "attributes": {},
#         "user": {
#             "userId": "amzn1.ask.account.AF4T2GZRHHPXIQPP7OZ4U5I556BGEUW6NAHDWLX6CXNXBH3WMKN7XADUAMYA7CDBKNKBY2YPDHGEAI3TRIJPTUIHHP7YEYKS7CEKZCKVAFUZMK5WN6KYNOGISYBFJTDZXPR7KEXIJR4BBTGCGTPOPY7GRNGGRKZGVWPG6RNH2GEUN3S2LQMFBEPFZJV2LKBFI2PGQGHRIYABNJQ"
#         }
#     },
#     "request": {
#         "type": "IntentRequest",
#         "requestId": "EdwRequestId.c9992add-a86d-4c52-980f-1f23577e5710",
#         "intent": {
#             "name": "Operatesomething",
#             "slots": {
#                 "device": {
#                     "name": "device",
#                     "value": "light"
#                 },
#                 "status": {
#                     "name": "status",
#                     "value": "on"
#                 }
#             }
#         },
#         "locale": "en-US",
#         "timestamp": "2017-08-20T12:23:04Z"
#     },
#     "context": {
#         "AudioPlayer": {
#             "playerActivity": "IDLE"
#         },
#         "System": {
#             "application": {
#                 "applicationId": "amzn1.ask.skill.c916f111-fe9e-4b9a-9fe4-33ea7b30eeb9"
#             },
#             "user": {
#                 "userId": "amzn1.ask.account.AF4T2GZRHHPXIQPP7OZ4U5I556BGEUW6NAHDWLX6CXNXBH3WMKN7XADUAMYA7CDBKNKBY2YPDHGEAI3TRIJPTUIHHP7YEYKS7CEKZCKVAFUZMK5WN6KYNOGISYBFJTDZXPR7KEXIJR4BBTGCGTPOPY7GRNGGRKZGVWPG6RNH2GEUN3S2LQMFBEPFZJV2LKBFI2PGQGHRIYABNJQ"
#             },
#             "device": {
#                 "supportedInterfaces": {}
#             }
#         }
#     },
#     "version": "1.0"
# }

# r = requests.post('http://127.0.0.1:8000/alexa/ask/', data=data)
# print(r.status_code)
# print(r.encoding)
# print(r.text)
# print(r.json())
from requests.auth import HTTPBasicAuth
import paho.mqtt.client as mqtt
import json

clientid = '777'
url = "http://127.0.0.1:8080/api/v2/nodes/emq@127.0.0.1/clients/{}".format(clientid)
r = requests.get(url, auth=HTTPBasicAuth('admin', 'admin'))
print(r.status_code)
# print(r.encoding)
# print(r.text)
# print(r.json())

data = r.json().get('result').get('objects')

print(data)
if data:
    print('on')
    pub_url = "http://127.0.0.1:8080/api/v2/mqtt/publish"
    post_data = {
        "topic": "$client/777",
        "payload": "open light",
    }
    r = requests.post(pub_url, data=json.dumps(post_data), auth=HTTPBasicAuth('admin', 'admin'))
    print(r.json())
else:
    print('no')

