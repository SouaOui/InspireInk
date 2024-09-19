from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profiles_pics')


    def __str__(self):
        return  f'{self.user.username} Profile'
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.mode in ("RGBA", "P"):  # If the image has transparency
            img = img.convert("RGB")   # Convert to RGB to remove transparency
            img.save(self.image.path)