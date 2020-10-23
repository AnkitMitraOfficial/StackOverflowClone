from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserform

# Create your views here.

def home(request):
    return render (request,'Contact/home.html')

def error_404_view(request, exception):
    return render(request,'Contact/404.html')

def landing(request):
    return render (request,'Contact/landing.html')
    
def signupuser(request):
    form = CreateUserform()

    if request.method == 'POST':
        form = CreateUserform(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render (request,'Authentication/signupuser.html')

def login(request):
    context = {}
    return render (request,'Authentication/loginuser.html')

def contact(request):
    return render (request,'Contact/contact.html')
