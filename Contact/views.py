from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from datetime import datetime
from .models import Contact
from django.contrib import messages
# Create your views here.

def home(request):
    return render (request,'Contact/home.html')

def error_404_view(request, exception):
    return render(request,'Contact/404.html')

def landing(request):
    return render (request,'Contact/landing.html')
    
def signupuser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
            
    context = {'form':form}
    return render (request,'Authentication/signupuser.html')

def loginuser(request):
    context = {}
    return render (request,'Authentication/loginuser.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request,'A new contact message has arrived!Check it out')
        return redirect('contact')

    
    return render (request,'Contact/contact.html')
