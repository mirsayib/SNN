from django.db import models
from django.contrib.auth.models import User
from PIL import Image 
from io import BytesIO

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = "default_zjgy3n.jpg", upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



    
    