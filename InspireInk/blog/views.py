from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'soumia ouzat',
        'title':'blog post 1',
        'content':'my first blog post',
        'date_posted': 'September 10, 2024'
    },
    {
        'author':'soumia ouzat',
        'title':'blog post 1',
        'content':'my second blog post',
        'date_posted': 'September 11, 2024'
    },
]

def home(request):
    context = {
        'posts': posts,
        'title': 'home'
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {'title': 'about'})