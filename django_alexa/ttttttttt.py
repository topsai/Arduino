#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import requests

data = {
    "session": {
        "new": False,
        "sessionId": "SessionId.31c4464a-b940-4be7-b6b4-3045bb15a93c",
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
        "requestId": "EdwRequestId.5699e1db-953c-4734-9b17-796eb9dc8679",
        "intent": {
            "name": "Operatesomething",
            "slots": {
                "status": {
                    "name": "status",
                    "value": "open"
                },
                "sb": {
                    "name": "sb",
                    "value": "light"
                }
            }
        },
        "locale": "en-US",
        "timestamp": "2017-08-19T12:51:39Z"
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
r = requests.post('http://127.0.0.1:8000/alexa/ask/', data=data)
print(r.status_code)
print(r.encoding)
print(r.text)
print(r.json())


aa = 'Traceback (most recent call last):\n  File "/usr/local/virtunlenvs/Arduino/virtual_evn/lib/python3.6/site-packages/rest_framework/views.py", line 486, in dispatch\n    response = handler(request, *args, **kwargs)\n  File "./django_alexa/views.py", line 111, in post\n    return self.handle_request(serializer.validated_data)\n  File "./django_alexa/views.py", line 86, in handle_request\n    _, slot = IntentsSchema.get_intent(app, intent_name)\n  File "./django_alexa/internal/intents_schema.py", line 32, in get_intent\n    raise InternalError(msg)\ndjango_alexa.internal.exceptions.InternalError: Unable to find an intent defined for \'Operatesomething.Operatesomething\'\n'