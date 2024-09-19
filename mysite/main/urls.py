from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView
    )
from . import views 

urlpatterns = [
    path("home/", views.home, name="home-page"),
    path("", views.index, name="index-page"),
    path('blog/', PostListView.as_view(), name='blog-page'), # <app>/<model>_<viewtype>.html
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/write/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),

]
