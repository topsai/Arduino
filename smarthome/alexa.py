#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from django_alexa.api import fields, intent, ResponseBuilder
import logging
import json

HOUSES = ("gryffindor", "hufflepuff", "ravenclaw", "slytherin")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='alexa.log',
                    filemode='a')

@intent
def LaunchRequest(session):
    """
    Hogwarts is a go
    ---
    launch
    start
    run
    begin
    open
    """
    logging.info(json.dumps(session))
    return ResponseBuilder.create_response(message="Welcome to Hog warts school of witchcraft and wizardry!",
                                           reprompt="What house would you like to give points to?",
                                           end_session=False,
                                           launched=True)


class PointsForHouseSlots(fields.AmazonSlots):
    house = fields.AmazonCustom(label="HOUSE_LIST", choices=HOUSES)
    points = fields.AmazonNumber()


class DoSomething(fields.AmazonSlots):
    sb = fields.AmazonCustom()
    status = fields.AmazonNumber()


@intent(slots=DoSomething)
def AddPointsToHouse(session, house, points):
    logging.info(json.dumps(session, house, points))
    """
    Direct response to add points to a house
    ---
    {points} {house}
    {points} points {house}
    add {points} points to {house}
    give {points} points to {house}
    """
    kwargs = {}
    kwargs['message'] = "{0} points added to house {1}.".format(points, house)
    if session.get('launched'):
        kwargs['reprompt'] = "What house would you like to give points to?"
        kwargs['end_session'] = False
        kwargs['launched'] = session['launched']
    return ResponseBuilder.create_response(**kwargs)

