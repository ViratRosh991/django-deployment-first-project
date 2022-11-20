from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def f11(req):
    return HttpResponse("<h2>Hello, Good Morning User...!! Have A Nice Day...</h2><hr/>")
    

