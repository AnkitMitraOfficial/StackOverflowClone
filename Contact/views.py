from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import CreateUserForm
from .models import Contact
from blog.models import Blog
from django.contrib import messages
# Create your views here.

def home(request):
    return render (request,'Contact/home.html')

def error_404_view(request, exception):
    return render(request,'Contact/404.html')

def landing(request):
    return render (request,'Contact/landing.html')

def search(request):
    query = request.GET['query']
    if len(query) > 50:
        blogs = Blog.objects.none()
    else:
        blogstittle = Blog.objects.filter(title__icontains=query)
        blogscontent = Blog.objects.filter(description__icontains=query)
        blogs = blogstittle.union(blogscontent)
    
    if blogs.count() == 0:
        messages.warning(request, 'Please fill the form correctly')
        
    params = {'blogs':blogs,'query':query}
    return render (request,'Contact/search.html', params)
    
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

        if len(name)<5 or len(desc)<20:
            messages.error(request,'Name must be 5 characters long,and the message should contains 20 characters!')
        else:
            contact = Contact(name=name,email=email,phone=phone,desc=desc)
            contact.save()
            messages.success(request,'Your message has been successfully sent!')
            return redirect('contact')
    return render (request,'Contact/contact.html')
