from django.contrib.auth.models import User
from django.db import models

class AnkietaOtw(models.Model):
    tytol = models.CharField(max_length=40)
    pytanie = models.CharField(max_length=500)
    data = models.DateTimeField(auto_now_add=True)
    kategoria = models.CharField(max_length=100)

    def __str__(self):
        return self.tytol



class OdpowiedzOtw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ankietaotw = models.ForeignKey(AnkietaOtw, on_delete=models.CASCADE)
    answer = models.TextField(max_length=700)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.ankietaotw.tytol}"
