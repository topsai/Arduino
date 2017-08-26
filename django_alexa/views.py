from __future__ import absolute_import
import logging
import traceback
from django.conf import settings
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from rest_framework.views import APIView
from .serializers import ASKInputSerializer
from .internal import ALEXA_APP_IDS, ResponseBuilder, IntentsSchema, validate_alexa_request, validate_response_limit

ALEXA_APP_ID_DEFAULT = "amzn1.ask.skill.c916f111-fe9e-4b9a-9fe4-33ea7b30eeb9"
# ALEXA_APP_ID_OTHER = "Your Amazon Alexa App ID OTHER"  # for each app
ALEXA_REQUEST_VERIFICATON = False  # Enables/Disable request verification

log = logging.getLogger(__name__)
# fh = logging.FileHandler('aaaaaaaaaa.log')
# fh.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# log.addHandler(fh)
# log.info('action')
# log = logging
# log.basicConfig(level=logging.INFO,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='aaaaaaaaaaa.log',
#                 filemode='a')
#
# log.info('actions....')


class ASKView(APIView):
    def handle_exception(self, exc):
        if settings.DEBUG:
            log.exception("An error occured in your skill.")
            # msg = "An error occured in your skill.  Please check the response card for details."
            msg = "en error"
            title = exc.__class__.__name__
            content = traceback.format_exc()
            data = ResponseBuilder.create_response(message=msg,
                                                   title=title,
                                                   content=content)
        else:
            msg = "An internal error occured in the skill."
            log.exception(msg)
            data = ResponseBuilder.create_response(message=msg)
        # If we need to return an error code, do so.
        # There is probably a better way of doing this, but this works. If anyone knows of a better way, please -
        # submit a correction
        try:
            error = exc.args[1]
            if error['error'] == 403:
                log.debug(data)
                return HttpResponseForbidden()
            elif error['error'] == 400:
                log.debug(data)
                return HttpResponseBadRequest()
            else:
                # If we are passed an error code we should probably do something more here, but for now - this works.
                return Response(data=data, status=HTTP_200_OK)
        except:
            return Response(data=data, status=HTTP_200_OK)

    def handle_request(self, validated_data):
        log.info("Alexa Request Body: {0}".format(validated_data))
        intent_kwargs = {}
        session = validated_data['session']
        app = ALEXA_APP_IDS[session['application']['applicationId']]
        if validated_data["request"]["type"] == "IntentRequest":
            intent_name = validated_data["request"]["intent"]["name"]
            for slot, slot_data in validated_data["request"]["intent"].get("slots", {}).items():
                slot_key = slot_data["name"]
                try:
                    slot_value = slot_data['value']
                except KeyError:
                    slot_value = None
                intent_kwargs[slot_key] = slot_value
        else:
            intent_name = validated_data["request"]["type"]
        _, slot = IntentsSchema.get_intent(app, intent_name)
        if slot:
            slots = slot(data=intent_kwargs)
            slots.is_valid()
            intent_kwargs = slots.data
        data = IntentsSchema.route(session, app, intent_name, intent_kwargs)
        return Response(data=data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # we have to save the request body because we need to set the version
        # before we do anything dangerous so that we can properly send exception
        # reponses and the DRF request object doesn't allow you to access the
        # body after you have accessed the "data" stream
        body = request.body
        print('body:', body)
        print('----------------------------------------')
        ResponseBuilder.set_version(request.data['version'])
        print('1----------------------------------------')
        validate_alexa_request(request.META, body)
        serializer = ASKInputSerializer(data=request.data)
        print('data', request.data)
        print('2----------------------------------------')
        serializer.is_valid(raise_exception=True)
        print('3----------------------------------------')
        return self.handle_request(serializer.validated_data)

    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
        log.debug("#" * 10 + "Start Alexa Request" + "#" * 10)
        response = super(ASKView, self).dispatch(request, *args, **kwargs)
        if response.status_code == 200:
            validate_response_limit(response.render().content)
        log.debug("#" * 10 + "End Alexa Request" + "#" * 10)
        return response


def update(request):
    if request.method == 'POST':
        # github的钩子被触发了
        data = request.POST
        print(data)

