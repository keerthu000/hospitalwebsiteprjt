from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    return render(request,'signup.html')
@login_required(login_url='index')
def loginpage(request):
    return render(request,'loginpage.html')
def register(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        print(firstname)
        lastname=request.POST['lname']
        dob=request.POST['date']
        gender=request.POST['inlineRadioOptions']
        email=request.POST['email']
        contact_num=request.POST['number']
        user=User.objects.create_user(username=firstname,first_name=firstname,last_name=lastname,email=email,password=email)  
        user.save()  
        return redirect('index')
    
    return render(request, 'register.html')
def appoinment(request):
    if request.method=="POST":
        firstname=request.POST['name']
        email=request.POST['email']
        
        user=auth.authenticate(request,username=firstname,password=email)
       
        if user is not None and user.is_authenticated:
            login(request,user)
            messages.info(request,'Appointment created successfully.')
            return redirect('loginpage')
        else:
            messages.info(request,'Please Register to make an appointment.')
            return redirect('signup')
               
        
    else:
        return redirect('loginpage')
    
def logout(request):
    request.session['userid']=""
    auth.logout(request)
    return redirect('index')
