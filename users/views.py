from django.shortcuts import render,redirect
from . models import Profile,Appointment
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from . forms import CustomUserCreationForm,ProfileForm,AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "user doesn't exist")
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('profiles')

        else:
            messages.error(request, "usename or password is incorrect")

    return render(request,'users/login_register.html')

def registerUser(request):
    form=CustomUserCreationForm()   
    
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'user sucessfully created')
            return redirect('login')
        else:
            messages.success(request,'something went wrong ')
    context={'data':'register','form':form}
    return render(request,'users/login_register.html',context)

def logoutUser(request):
    logout(request)
    messages.error(request, "been loggedout ")
    return redirect('login')

def profiles(request):
    return render(request, 'users/profiles.html',)
