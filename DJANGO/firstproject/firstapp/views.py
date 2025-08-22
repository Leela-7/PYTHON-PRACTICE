from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def display(request):
    s='<h1>Hi Everyone!</h1>'
    return HttpResponse(s)