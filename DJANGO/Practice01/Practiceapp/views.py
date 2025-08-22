from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
# # Create your views here.
# def display(request):
#     current_time = datetime.now()
#     formatted_time = current_time.strftime("server time: %Y-%m-%d %H:%M:%S")
#     return HttpResponse(formatted_time)


def display2(request):
    date = datetime.now()
    msg='<h1>Hi Everyone! Good Evening!</h1>'
    msg+='Server time is:'+str(date)
    return HttpResponse(msg)