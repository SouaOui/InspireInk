from django.urls import path

from . import views 

urlpatterns = [
    path("home/", views.home, name="home-page"),
    path("", views.index, name="index-page"),
    path('blog/', views.blog, name='blog-page'),
]
