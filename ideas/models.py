from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ideas(models.Model):
    title_en = models.TextField(max_length=30, null=True, blank=True)
    desc_en = models.TextField(max_length=300, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="ideas/uploaded", null=True)
    
    
    vocals = models.BooleanField(default=False)
    acoustic = models.BooleanField(default=False)
    electronic = models.BooleanField(default=False)
    drums = models.BooleanField(default=False)
    rap = models.BooleanField(default=False)
    beat = models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return f'{self.title_en} - {self.date.date()} - id: {self.id} - user: {self.user.username}'