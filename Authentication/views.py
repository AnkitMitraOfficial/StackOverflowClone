from django.shortcuts import render, redirect

# Create your views here.

def profilr(request):
    return render (request, 'Authentication/profile.html')
