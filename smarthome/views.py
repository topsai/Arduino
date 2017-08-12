from django.shortcuts import render, HttpResponse
import json

# Create your views here.


def index(request):
    # test
    d = {
        "version": "1.0",
        "response": {
            "outputSpeech": {"type": "PlainText", "text": "Text to speak back to the user."},  # text中是语音回复的内容
            "card": {  # 显示在Alexa APP中的内容
                "type": "Simple",
                "title": "Example of the Card Title",
                "content": "Example of card content. This card has just plain text content.\n"
                           "The content is formatted with line breaks to improve readability."
            }
        }
    }
    return HttpResponse(json.dumps(d))
