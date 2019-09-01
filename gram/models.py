from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):    
    bio = models.CharField(max_length = 100)
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, default=1)
    

    def save_profile(self):
        self.save()

    @classmethod
    def display_profile(cls):
        profiles=cls.objects.get(pk=1)
        return profiles

    def delete_profile(self):
        return self.delete()

    @classmethod
    def find_username(cls, search_term):
        profiles=cls.objects.filter(user__username__icontains=search_term)
        return profiles 

    def __str__(self):
        return self.user.username