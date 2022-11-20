"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from FirstApp import views
from MultiViewApp import views as v1   ##new-App views
#Approach-1:
from App1.views import f11;
from App2.views import f22;
#Approach-2
from App1 import views as v2
from App2 import views as v3

#Approach-1:
from FirstApp import views;
#Approach-2:
from FirstApp.views import demo;


from django.urls import re_path;

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('Welcome/',views.display),
    #path('Welcome2/',views.show),
    #path('hello/',views.hello),
    #path('dtime/',views.senddatetime),
    path('mrng/',v1.f1),
    path('aftr/',v1.f2),
    path('evng/',v1.f3),
#Approach-1:
    path('hello1/',f11),
	path('datetime1/',f22),
    
#Approach-2:
	path('hello/',v2.f11),
    path('datetime/',v3.f22),
	
    
#demo()view of views.py
#Approach-1:
    path('firstdemo/',views.demo),
    path('seconddemo/',views.demo),
    path('thirddemo/',views.demo),
#Approach-2:
    path('firstdemo1/',demo),
    path('seconddemo1/',demo),
    path('thirddemo1/',demo),

#Default-HomePage:
    re_path("^.*$",views.homepage)
]

