from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Message

# Create your views here.
def service(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contactus_info = Message.objects.create()
        contactus_info.firstname = fname
        contactus_info.email = email
        contactus_info.subject = subject
        contactus_info.message = message

        contactus_info.save()
        return redirect('home')
    return render(request, 'Contact.html')

def index(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contactus_info = Message.objects.create()
        contactus_info.firstname = fname
        contactus_info.email = email
        contactus_info.subject = subject
        contactus_info.message = message

        contactus_info.save()
        return redirect('home')
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        my_info = User.objects.create_user(username, email, pass1)
        my_info.first_name = fname
        my_info.last_name = lname
        my_info.phone_number = phone
        my_info.save()
        return redirect('home')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password = pass1)

        if user is not None:
            login(request, user)
            return redirect('home')

        else :
            messages.error(request, "Check your login info!!")
            return redirect('signin')

    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'You logged out successfully')
    return redirect('index')

