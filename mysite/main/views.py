from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
# to ensure that you are the one who owns this post 'UserPassesTestMixin'

from .models import Post

def home(request):
    return render(request, "home.html")


def index(request):
    return render(request, "index.html")

def login(request):
	return render(request, "login.html")

def blog(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, "blog.html", context)

class PostListView(ListView):
     model = Post
     template_name = 'blog.html'
     context_object_name = 'posts'
     ordering = ['-date_posted'] # reverse the way the posts are sorted from new to old

class PostDetailView(DetailView):
     model = Post
     template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
         post = self.get_object()
         if self.request.user == post.author:
            return True
         else:
            return False
    
class PostUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
         post = self.get_object()
         if self.request.user == post.author:
            return True
         else:
            return False
         

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('home-page')

    def test_func(self):
         post = self.get_object()
         if self.request.user == post.author:
            return True
         else:
            return False