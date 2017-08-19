#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from django_alexa.internal.intents_schema import IntentsSchema

ALEXA_APP_ID_DEFAULT = "amzn1.ask.skill.c916f111-fe9e-4b9a-9fe4-33ea7b30eeb9"
ALEXA_APP_ID_OTHER = "Operatesomething"  # "Your Amazon Alexa App ID OTHER"  # for each app
ALEXA_REQUEST_VERIFICATON = False  # Enables/Disable request verification


def Operatesomething():
    print('Operatesomething')

print('regist----')
IntentsSchema.register(app="light", func=Operatesomething(), intent="Operatesomething")
