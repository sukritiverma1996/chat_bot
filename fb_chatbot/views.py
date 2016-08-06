from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

class MyQuoteBotView(generic.View):
    def get(self, request, *args, **kwargs):
        try:
            # that number is your webhook token which youll set up in a bit
            if self.request.GET['hub.verify_token'] == '8447789934':
                return HttpResponse(self.request.GET['hub.challenge'])
            else:
                return HttpResponse('Error, invalid token')
        except:
            return HttpResponse('Error, invalid token')

# Create your views here.

def hello_world(request):
    return HttpResponse("<b><i>Hello World</i></b>")

def hello(request):
    return HttpResponse("Hey Hey!")