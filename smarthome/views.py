from django.shortcuts import render, HttpResponse
import json
import logging

# Create your views here.
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='alexa.log',
                    filemode='a')


def index(request):
    if request.method == "POST":
        logging.info(request.POST)

    # test
    d = {
        "version": "1.0",
        "response": {
            "outputSpeech": {"type": "PlainText", "text": "nong sha lei"},  # text中是语音回复的内容
            "card": {  # 显示在Alexa APP中的内容
                "type": "Simple",
                "title": "Example of the Card Title",
                "content": "Example of card content. This card has just plain text content.\n"
                           "The content is formatted with line breaks to improve readability."
            }
        }
    }
    return HttpResponse(json.dumps(d))
