from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):    
    bio = models.CharField(max_length = 100)
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, default=1)
    

    def save_profile(self):
        self.save()