from __future__ import absolute_import
from .api import intent, ResponseBuilder
from django_alexa.internal import fields


@intent
def LaunchRequest(**kwargs):
    """
    Default Start Session Intent
    ---
    launch
    open
    resume
    start
    run
    load
    begin
    """
    return ResponseBuilder.create_response(message="Welcome.",
                                           reprompt="What would you like to do next?",
                                           end_session=False)


@intent
def CancelIntent(**kwargs):
    """
    Default Cancel Intent
    ---
    cancel
    """
    return ResponseBuilder.create_response(message="Canceling actions not configured!",
                                           reprompt="What would you like to do next?",
                                           end_session=False)


@intent
def StopIntent(**kwargs):
    """
    Default Stop Intent
    ---
    stop
    end
    nevermind
    """
    return ResponseBuilder.create_response(message="Stopping actions not configured!")


@intent
def HelpIntent(**kwargs):
    """
    Default Help Intent
    ---
    help
    info
    information
    """
    return ResponseBuilder.create_response(message="No help was configured!")


@intent
def SessionEndedRequest(**kwargs):
    """
    Default End Session Intent
    ---
    quit
    """
    return ResponseBuilder.create_response()


class PointsForHouseSlots(fields.AmazonSlots):
    status = fields.AmazonEvent()
    device = fields.AmazonDevice()

    def get_fields(self):
        return {'status': self.status, 'device': self.device}

    def __init__(self, data):
        print('PointsForHouseSlots-data', data)


@intent(slots=PointsForHouseSlots, app='light')
def Operatesomething(session, house, points):
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
