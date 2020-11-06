from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
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
    if len(query) > 15:
        messages.warning(request, 'Search query must be a maximum of 15 characterss')
        blogs = Blog.objects.none()
    if len(query) <5:
        messages.warning(request, 'Search query must be minimum 5 characters')
        blogs = Blog.objects.none()

    else:
        blogstittle = Blog.objects.filter(title__icontains=query)
        blogscontent = Blog.objects.filter(description__icontains=query)
        blogs = blogstittle.union(blogscontent)
    
    if blogs.count() == 0:
        messages.warning(request, 'No search results found,Kindly refine your query')
        
    params = {'blogs':blogs,'query':query}
    return render (request,'Contact/search.html', params)

def signupuser(request):
    if request.method == 'POST':
        return HttpResponse ('Hello World')

    else:
        return HttpResponse ('Hello') 

def loginuser(request):
    context = {}
    return render (request,'Authentication/loginuser.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if len(desc) < 20:
            messages.error(request,'The message should contain atleast 20 characters!')
        else:
            contact = Contact(name=name,email=email,phone=phone,desc=desc)
            contact.save()
            messages.success(request,'Your message has been successfully sent!')
            return redirect('contact')
    return render (request,'Contact/contact.html')
