from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def f22(req):
    time = datetime.datetime.now()
    return HttpResponse("<h2>Hello User..!!<br ><br />Server Date & Time ::"+str(time)+"</h2><hr/>")
