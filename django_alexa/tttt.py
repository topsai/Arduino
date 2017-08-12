#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import requests

data = {
    "session": {
        "new": True,
        "sessionId": "SessionId.c16a62d0-185f-4e1a-a90c-431ac9c1be25",
        "application": {
            "applicationId": "amzn1.ask.skill.c916f111-fe9e-4b9a-9fe4-33ea7b30eeb9"
        },
        "attributes": {},
        "user": {
            "userId": "amzn1.ask.account.AF4T2GZRHHPXIQPP7OZ4U5I556BGEUW6NAHDWLX6CXNXBH3WMKN7XADUAMYA7CDBKNKBY2YPDHGEAI3TRIJPTUIHHP7YEYKS7CEKZCKVAFUZMK5WN6KYNOGISYBFJTDZXPR7KEXIJR4BBTGCGTPOPY7GRNGGRKZGVWPG6RNH2GEUN3S2LQMFBEPFZJV2LKBFI2PGQGHRIYABNJQ"
        }
    },
    "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.0e9fcb90-ef07-406e-b566-e24796c6a1dd",
        "intent": {
            "name": "Operatesomething",
            "slots": {
                "status": {
                    "name": "status",
                    "value": "on"
                },
                "sb": {
                    "name": "sb",
                    "value": "light"
                }
            }
        },
        "locale": "en-US",
        "timestamp": "2017-08-12T13:38:00Z"
    },
    "context": {
        "AudioPlayer": {
            "playerActivity": "IDLE"
        },
        "System": {
            "application": {
                "applicationId": "amzn1.ask.skill.c916f111-fe9e-4b9a-9fe4-33ea7b30eeb9"
            },
            "user": {
                "userId": "amzn1.ask.account.AF4T2GZRHHPXIQPP7OZ4U5I556BGEUW6NAHDWLX6CXNXBH3WMKN7XADUAMYA7CDBKNKBY2YPDHGEAI3TRIJPTUIHHP7YEYKS7CEKZCKVAFUZMK5WN6KYNOGISYBFJTDZXPR7KEXIJR4BBTGCGTPOPY7GRNGGRKZGVWPG6RNH2GEUN3S2LQMFBEPFZJV2LKBFI2PGQGHRIYABNJQ"
            },
            "device": {
                "supportedInterfaces": {}
            }
        }
    },
    "version": "1.0"
}
d = {}
# r = requests.post("http://127.0.0.1:8000/alexa/ask/", data=d)
r = requests.post("https://www.codefarmer.site/alexa/ask/", data=data)
print(r.text)

