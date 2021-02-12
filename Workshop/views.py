from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def static(request):
    return HttpResponse("<center><h1 style='color:blue;background-color:pink;margin-left:120px;margin-right:120px;padding:15;border-radius:100px;'><i><h1>This is static page<h1><i></h1><center>")

def dynamicstr(request,name):
    return HttpResponse("<center><h3>hiii "+name+"<br>THis is dynamic string url<h3><center>")
def dynamicint(request,id):
    return HttpResponse("<center><h3>hiii {} <br>This is dynamic intger url<h3></center>".format(id)) 
def dynamicstrint(request,name,id):
    return HttpResponse("<center><h3>Name is <br>"+name+" pin is {} <br>This is dynamic  string intger url<h3></center>".format(id))        