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
{"version":"1.0","response":{"shouldEndSession":true,"outputSpeech":{"type":"PlainText","text":"An error occured in your skill.  Please check the response card for details."},"card":{"type":"Simple","title":"JSONDecodeError","content":"Traceback (most recent call last):\n  File \"/usr/local/virtunlenvs/Arduino/virtual_evn/lib/python3.6/site-packages/rest_framework/views.py\", line 486, in dispatch\n    response = handler(request, *args, **kwargs)\n  File \"./django_alexa/views.py\", line 106, in post\n    validate_alexa_request(request.META, body)\n  File \"./django_alexa/internal/validation.py\", line 118, in validate_alexa_request\n    timestamp = json.loads(request_body)['request']['timestamp']\n  File \"/usr/local/python3/lib/python3.6/json/__init__.py\", line 354, in loads\n    return _default_decoder.decode(s)\n  File \"/usr/local/python3/lib/python3.6/json/decoder.py\", line 339, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n  File \"/usr/local/python3/lib/python3.6/json/decoder.py\", line 357, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)\n"}},"sessionAttributes":{}}
