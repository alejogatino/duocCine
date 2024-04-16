from django.shortcuts import render
from django.conf.urls.static import static

# Create your views here.

def home(request):
     return render(request, 'core/home.html')

def posts(request):
     return render(request, 'core/posts.html')