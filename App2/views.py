from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def stat(request):
    return HttpResponse('I am from App 2')
def home(request):
    return HttpResponse("<h2><b><i>I am from app2 urls<i><b><h2>") 
def index(request):
    value=random.randint(1,100)
    return render(request,'index.html',{'name':value})
def student(request):
    details={'name':'Sunitha','number':44,'branch':'cse'}
    return render(request,"student_info.html",{'details':details})
def value(request,val):
    a=[]
    for i in  range(1,val+1):
        a.append(i)
    return render(request,"value.html",{'value':a})
def table(request,v):
    a=[]
    for i in range(1,11):
        a.append(i*v)
    return render(request,'table.html',{'array':a,'v':v})