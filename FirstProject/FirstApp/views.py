from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(req):        #view-func
    print("Welcome/url is request & display() is executed");
    ss = "<center><h2 style='color:Blue;'>Hello User, Welcome to Django First-Project First-App</h2><hr  /><center>";
    return HttpResponse(ss);
    
    
def show(req):
    ss = '''<!--
	HTML Webpage to display 'Welcome-Message' with different Headings 
	(F:\SAISIR\HTML\Welcome.html)
-->
    
<html>
	<head>
		<title>***Weclome-Page***</title>
		<style>
			h1{
				color:Blue;
			}
			h2{
				color:Green;
			}
			h3{
				color:Red;
			}
			h4{
				color:Red;
			}
			h5{
				color:Red;
			}
			h6{
				color:Blue;
			}
			h1,h3,h5{
				background-color:Grey;
			}
			h2,h4,h6{
				background-color:lightgreen;
			}
		</style>
	</head>
	<body>
		<center>
			<h1>Welcome To Django Html WebPage</h1>
			<hr color="Black" width="95%"/>
			<h2>Welcome To Django Html WebPage</h2>
			<hr color="Black" width="85%"/>
			<h3>Welcome To Django Html WebPage</h3>
			<hr color="Black" width="75%"/>
			<h4>Welcome To Django Html WebPage<h4>
			<hr color="Black" width="65%"/>
			<h5>Welcome To Django Html WebPage<h5>
			<hr color="Black" width="55%"/>
			<h6>Welcome To Django Html WebPage<h6>
			<hr color="Black" width="45%"/>
		<center>
	</body>
</html>''';
    
    return HttpResponse(ss);
    
    
def hello(request):
    print("hello/ url is requested & hello() is executed");
    ss = '''
    <html>
        <head>
            <title>Hello WebPage</title>
                <style>
                    h1{
                        color:Blue;
                    }
                    h2{
                        color:Green;
                    }
                    h3{
                        color:Red;
                    }
                    h1,h2,h3{
                        background-color:plum;
                        width:60%;
                        border:2px Solid Brown;
                    }
                                  
                </style>
        </head>
            
            <body>
                    <center>
                            <h1>Hello User...!!!</h1>
                            <hr color='brown' width='80%'/>
                            <h2>Welcome To Django</h2>
                            <hr color='brown' width='80%'>
                            <h3>Have A Nice Day...</h3>
                            <hr color='brown' width='80%'>
                    </center>
            </body>
    </html>''';
    return HttpResponse(ss);
    
 
 
import time;
def senddatetime(request):
    print("dtime/url is required & seddatetime() is executed");
    ct = time.ctime()
    print("Client Request Date & time on server ::",ct)
    ss ='''
    
    <html>
        <head>
            <title>Date-Time Webpage</title>
            <style>
                    h1{
                        color:Blue;
                    }
                    h2{
                        color:Green;
                    }
                    h3{
                        color:Red;
                    }
                    h1,h2,h3{
                        background-color:Grey;
                        
                    }
            </style>
        </head>
        <body>
            <center>
                <h1>Welcome To Django-User...!!!</h1>
                <hr color='brown' width='80%'/>
                <h2>Server-Date & Time :: </h2>
				<hr color='brown' width='80%'/>
				<h3>''',ct,'''</h3>
            </center>
        </body>
    </html>
    ''';
    return HttpResponse(ss);
    
    
    
def demo(req):  
	print("mulitple-Requests-URLs same respose");
	htmldata='''<center>
		<h1>Welcome Demo User!!!</h1>
		<hr />
		<h2>This is Same-Output for diff-mulitple-Requests-URLs</h2>
		<hr />
		<h3>Have a Great Day...</h3>
		</center>''';
	return HttpResponse(htmldata);

    
    
#Creating Default-Home-Page***
def homepage(request):
    htmldata='''<center>
            <h1>Welcome To DEFAULT HOME-PAGE!!!</h1>
            <hr />
            <h2>Your Request Page-Is-Not-Found</h2>
            <hr />
            <h3>Plz Try Other URL or LINKS!!!</h3>
            <hr />
        </center>''';
    return HttpResponse(htmldata);
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    