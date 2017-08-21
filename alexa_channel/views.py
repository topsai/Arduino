from django.shortcuts import render, HttpResponse
from channels import Channel


# Create your views here.
def test(request):
    print('talk')
    Channel('send-invite').send({'text': 'test'})
    return HttpResponse("ok")
