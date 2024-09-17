from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    return render(request, "home.html")

def login(request):
	return render(request, "login.html")

def blog(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, "blog.html", context)