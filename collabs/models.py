from django.db import models
from django.contrib.auth.models import User

class Collab(models.Model):
    title = models.TextField(max_length=30)
    desc = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    download_pack = models.FileField(upload_to='collabs/downloads', null=True, blank=True)
    
    def __str__(self):
        return f'{self.title} - {self.date.date()}'
    
class CollabSub(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collab = models.ForeignKey(Collab, on_delete=models.CASCADE)
    title = models.TextField(max_length=40, null=True)
    msg = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='collabs/downloads', null=True)
    sprawdzone = models.BooleanField(default=False)
    odpowiedz = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.collab.title}"

# Create your models here.
