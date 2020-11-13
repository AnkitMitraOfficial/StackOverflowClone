from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render (request, 'StackoverflowClone/home.html')


def about(request):
    return render (request, 'StackoverflowClone/about.html')

