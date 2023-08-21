from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=150)

    def __str__(self):
        return self.user.username

# Create your models here.
