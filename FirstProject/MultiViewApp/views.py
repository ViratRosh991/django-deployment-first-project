from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
    
#==>> Single-application with multiple views (MultiViewsApp)

def f1(req):
    return HttpResponse("<h2>Good Morning User...!!! Have A Nice Day...</h2><hr/>")
    
def f2(req):
    return HttpResponse("<h2>Good Afternoon User...!!! Hope You Are Doing Good...</h2><hr/>")

def f3(req):
    return HttpResponse("<h2> Good Evening User...!!! How Was Your Day...</h2><hr/>")
