from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.all_blog,name='blog'),
]