from django.urls import path

from . import views 

urlpatterns = [
    path("", views.home, name="home-page"),	
    path('blog/', views.blog, name='blog-page'),
]
