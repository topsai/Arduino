#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from django_alexa.api import fields, intent, ResponseBuilder

HOUSES = ("gryffindor", "hufflepuff", "ravenclaw", "slytherin")

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
    return ResponseBuilder.create_response(message="Welcome to Hog warts school of witchcraft and wizardry!",
                                           reprompt="What house would you like to give points to?",
                                           end_session=False,
                                           launched=True)


class PointsForHouseSlots(fields.AmazonSlots):
    house = fields.AmazonCustom(label="HOUSE_LIST", choices=HOUSES)
    points = fields.AmazonNumber()


@intent(slots=PointsForHouseSlots)
def AddPointsToHouse(session, house, points):
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