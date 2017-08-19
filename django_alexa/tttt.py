#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import requests

# data = {
#     "session": {
#         "new": True,
#         "sessionId": "SessionId.c16a62d0-185f-4e1a-a90c-431ac9c1be25",
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
#         "requestId": "EdwRequestId.0e9fcb90-ef07-406e-b566-e24796c6a1dd",
#         "intent": {
#             "name": "Operatesomething",
#             "slots": {
#                 "status": {
#                     "name": "status",
#                     "value": "on"
#                 },
#                 "sb": {
#                     "name": "sb",
#                     "value": "light"
#                 }
#             }
#         },
#         "locale": "en-US",
#         "timestamp": "2017-08-12T13:38:00Z"
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
# d = {}
# # r = requests.post("http://127.0.0.1:8000/alexa/ask/", data=d)
# r = requests.post("https://www.codefarmer.site/alexa/ask/", data=data)
# print(r.text)

'request' 'intent' 'name'  # AppName
# 'request' 'intent' 'slots' ['slotsname'] 'value'  #  'slots_value'
a = {'version': '1.0',
     'session': {'new': True,
                 'sessionId': 'amzn1.echo-api.session.31912457-c6e0-49e9-9847-fbeb3b0dfb70',
                 'application': {'applicationId': 'amzn1.ask.skill.c916f111-fe9e-4b9a-9fe4-33ea7b30eeb9'},
                 'user': {
                    'userId': 'amzn1.ask.account.AF4T2GZRHHPXIQPP7OZ4U5I556BGEUW6NAHDWLX6CXNXBH3WMKN7XADUAMYA7CDBKNKBY2YPDHGEAI3TRIJPTUIHHP7YEYKS7CEKZCKVAFUZMK5WN6KYNOGISYBFJTDZXPR7KEXIJR4BBTGCGTPOPY7GRNGGRKZGVWPG6RNH2GEUN3S2LQMFBEPFZJV2LKBFI2PGQGHRIYABNJQ',
                    'permissions': {}
                        }
                 },
     'context': {'AudioPlayer': {'playerActivity': 'IDLE'},
                 'System': {
                        'application': {'applicationId': 'amzn1.ask.skill.c916f111-fe9e-4b9a-9fe4-33ea7b30eeb9'},
                        'user': {
                        'userId': 'amzn1.ask.account.AF4T2GZRHHPXIQPP7OZ4U5I556BGEUW6NAHDWLX6CXNXBH3WMKN7XADUAMYA7CDBKNKBY2YPDHGEAI3TRIJPTUIHHP7YEYKS7CEKZCKVAFUZMK5WN6KYNOGISYBFJTDZXPR7KEXIJR4BBTGCGTPOPY7GRNGGRKZGVWPG6RNH2GEUN3S2LQMFBEPFZJV2LKBFI2PGQGHRIYABNJQ',
                        'permissions': {}},
                         'device': {
                            'deviceId': 'amzn1.ask.device.AHHYDTEIY7R4RHLY2WIU2MEIHMNRK3SENSQ3KWR3GZRS5H7EPB653R3ZWRJGEX256A2UKK53S2ITIETB4SEXYGIZEGTFMYVGN5PWBYRJRYJACTAVULG54RWVJ2L2QRNC53IYYVXUAZYQ3ZZ2GXHGFNDDO4ZQ',
                            'supportedInterfaces': {'AudioPlayer': {}}
                            },
                        'apiEndpoint': 'https://api.amazonalexa.com'
                        }
                 },
     'request': {'type': 'IntentRequest', 'requestId': 'amzn1.echo-api.request.c5fef716-0952-45b3-88ec-dcf7bead6726',
                 'timestamp': '2017-08-12T16:01:10Z',
                 'locale': 'en-US',
                 'intent': {'name': 'Operatesomething',
                            'confirmationStatus': 'NONE',
                            'slots': {
                                 'status': {'name': 'status',
                                            'value': 'on',
                                            'resolutions': {'resolutionsPerAuthority': [
                                                                {
                                                                 'authority': 'amzn1.er-authority.echo-sdk.amzn1.ask.skill.c916f111-fe9e-4b9a-9fe4-33ea7b30eeb9.status',
                                                                 'status': {
                                                                            'code': 'ER_SUCCESS_MATCH'
                                                                            },
                                                                 'values': [
                                                                        {
                                                                         'value': {
                                                                             'name': 'on',
                                                                             'id': 'ed2b5c0139cec8ad2873829dc1117d50'}
                                                                        }]
                                                                }]
                                                            },
                                                    'confirmationStatus': 'NONE'
                                            },
                                 'sb': {'name': 'sb',
                                        'value': 'light',
                                        'resolutions': {
                                                         'resolutionsPerAuthority': [{
                                                                                     'authority': 'amzn1.er-authority.echo-sdk.amzn1.ask.skill.c916f111-fe9e-4b9a-9fe4-33ea7b30eeb9.sb',
                                                                                     'status': {'code': 'ER_SUCCESS_MATCH'},
                                                                                     'values': [
                                                                                         {'value': {'name': 'light',
                                                                                                    'id': '2ac43aa43bf473f9a9c09b4b608619d3'}}
                                                                                        ]}
                                                                                    ]
                                                         },
                                                                                  'confirmationStatus': 'NONE'
                                        }
                                    }
                            },
                 'dialogState': 'STARTED'}
     }

print(type(a))
