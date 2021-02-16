from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
from App2.models import Student,Registration
from App2.forms import StudentForm
from django.contrib import messages

# Create your views here.
def stat(request):
    return HttpResponse('I am from App 2')
def home(request):
    return HttpResponse("<h2><b><i>I am from app2 urls<i><b><h2>") 
# def index(request):
#     value=random.randint(1,100)
#     return render(request,'index.html',{'name':value})
# def student(request):
#     details={'name':'Sunitha','number':44,'branch':'cse'}
#     return render(request,"student_info.html",{'details':details})
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
def sample(request):
    return render(request,'sample.html')
def register(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        # lname = request.POST.get('lname')
        email= request.POST.get('email')
        MobileNo= request.POST.get('MobileNo')
        gender=request.POST.get('gender')
        rollno=request.POST.get('rlno')
        # context={'fname':fname,'email':email,'MobileNo':MobileNo,'gender':gender}
        Student.objects.create(FullName=fname,RollNo=rollno,EmailId=email,MobileNo=MobileNo,Gender=gender)
        return redirect('details')
        return render(request,'register.html')  
def display_details(request):
    data=Student.objects.all()
    return render(request,'result.html',{'data':data})   
def update_details(request,id):
    data=Student.objects.get(id=id)
    if request.method=='POST':
        data.FullName = request.POST.get('fname')
        data.EmailId= request.POST.get('email')
        data.MobileNo= request.POST.get('MobileNo')
        data.Gender=request.POST.get('gender')
        data.RollNo=request.POST.get('rlno')
        data.save()
        return redirect('details')
    return render(request,'update.html',{'data':data})
def delete(request, id):
	Student.objects.get(id=id).delete()
	return redirect('details')

def signup(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Registration is Sucesfully completed...... ")
            return redirect('signup')
    form=StudentForm()
    return render(request,"signup.html",{'form':form}) 
def registration(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        email=request.POST.get('email')
        im=request.FILES['image']
        Registration.objects.create(Username=uname,Email=email,PassWord=password,Image=im)
        return HttpResponse("ok....")
    return render(request,'registration.html')
