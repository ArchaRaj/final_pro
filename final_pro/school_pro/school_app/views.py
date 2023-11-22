from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from  django.http import HttpResponse
from .models import Table1, Option

from .forms import Tableform

# Create your views here.
def demo(request):
    return render(request,'index.html')

def login(request):

    if request.method == 'POST':
        uname = request.POST['uname1']
        password = request.POST['pass1']
        user = auth.authenticate(username=uname, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('login2')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')


    return render(request,'login.html')

def login2(request):

    return render(request,'login2.html')
def register(request):
    if request.method=='POST':
        username=request.POST['unamer1']
        password=request.POST['passr1']
        cpassword=request.POST['passr2']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            else:
                u=User.objects.create_user(username=username,password=password)
                u.save()
                print("User registered")
                return redirect('login')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')

    return render(request,"register.html")
def login3(request):
    # if request.method=='POST':
    #     form=Tableform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         message = "Order Confirmed"
    #         return render(request,"login3.html",{'message':message})
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']

        dob = request.POST['date']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']
        department = request.POST['subject']
        course = request.POST['topic']
        purpose = request.POST['purpose']
        materiall = map(int,request.POST.getlist('material'))

        if Table1.objects.filter(email=email).exists():
            messages.info(request, "Already registered")
            return redirect('login3')
        else:
            ins=Table1.objects.create(name=name, email=email,dob=dob,age=age,gender=gender,phone=phone,address=address,department=department,course=course,purpose=purpose,login_person=request.user)
            material=Option.objects.filter(id__in=materiall)
            ins.material.set(material)
            ins.save()
            message="Order Confirmed"
            return render(request,"login3.html",{'message':message})

    return render(request,"login3.html")