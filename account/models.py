from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    
    vocals = models.BooleanField(default=False)
    production = models.BooleanField(default=False)
    mixmaster = models.BooleanField(default=False)
    instrument = models.BooleanField(default=False)
    
    pic = models.ImageField(upload_to='users/images/', blank=True, null=True)
    bio = models.TextField(max_length=150, blank=True)
    social1 = models.CharField(max_length=50, null=True, blank=True)
    social2 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username