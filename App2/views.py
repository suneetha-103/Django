from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
from App2.models import Student,Registration,UserProfile
from App2.forms import StudentForm,RegisterForm
from django.contrib import messages
from DjangoProject import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
 

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
        sub='reg welcome message'
        body='Username'+uname+'PassWord'+password
        receiver=email
        sender=settings.EMAIL_HOST_USER
        send_mail(sub,body,sender,[receiver])
        # return HttpResponse("ok....")
        return redirect('showdata')
    return render(request,'registration.html')
def showdata(request):
    data=Registration.objects.all()
    return render(request,'showdata.html',{'data':data})
def signupform(request):
    if request.method=='POST':
        sform=RegisterForm(request.POST)
        if sform.is_valid:
            sform.save()
            return HttpResponse("Succesfully Rgistered")
    else:
        sform=RegisterForm()
        return render(request,'signupform.html',{'sform':sform})    
def profile(request):
    user = user.objects.get(request.user.id)
    pro = UserProfile.objects.get(user=user) 
    return render(request,'profile.html',{'user':user,'pro':pro})    