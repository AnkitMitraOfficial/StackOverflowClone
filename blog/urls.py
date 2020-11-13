from django.urls import path, include
from .import views

app_name = 'blog'
#If you want to refer to any blog url you have to this else error
#{% url 'blog:blog' %},because I have set the app_name to 'blog'

urlpatterns = [
    path('',views.all_blog,name='blog'),
    path('<int:blog_id>/', views.detail, name='detail'),
]