from __future__ import absolute_import
from .api import intent, ResponseBuilder
from django_alexa.internal import fields
import redis
import requests
from requests.auth import HTTPBasicAuth
import json


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
        self.data = data

    def is_valid(self):
        # 验证没做
        return True


@intent(slots=PointsForHouseSlots, app='light')
def Operatesomething(session, device, status, ):
    """
    Direct response to add points to a house
    ---
    {points} {house}
    {points} points {house}
    add {points} points to {house}
    give {points} points to {house}
    """
    kwargs = {}
    # data = {'text': device + ',' + status}
    # from alexa_channel.consumers import all_device
    # print(all_device)
    # r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    # all_device = r.get('all_device')
    # dd = eval(all_device.decode())
    #
    # from channels import Group, channel
    # # channel.Channel(dd.get('smarthome')).send({'text': data})
    # from alexa_channel.consumers import all_device
    #
    # if all_device.get('smarthome'):
    #     channel.Channel(all_device.get('smarthome')).send(data)
    #     kwargs['message'] = "your {0} is {1}.".format(device, status)
    # else:
    #     kwargs['message'] = "your device not online."
    ddd = ""

    if status == "on" or status == "open":
        s = "open "
        ddd = s+device
    elif status == "off" or status == "close":
        s = "close "
        ddd = s + device
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
            "payload": ddd,
        }
        r = requests.post(pub_url, data=json.dumps(post_data), auth=HTTPBasicAuth('admin', 'admin'))
        print(r.json())
        kwargs['message'] = "your {0} is {1}.".format(device, status)
    else:
        kwargs['message'] = "your device not online."

    if session.get('launched'):
        kwargs['reprompt'] = "ok !"
        kwargs['end_session'] = True
        kwargs['launched'] = session['launched']
    return ResponseBuilder.create_response(**kwargs)
