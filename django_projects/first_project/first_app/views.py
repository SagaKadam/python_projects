from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse('Hello, Django')

def display_date_time(request):
    dt = datetime.datetime.now()
    date_time = '<b>Current date and time is: </b>'+str(dt)
    return HttpResponse(date_time)