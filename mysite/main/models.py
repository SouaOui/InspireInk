from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100, default="not-listed")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} + ' ' + {self.content}" 
    
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})