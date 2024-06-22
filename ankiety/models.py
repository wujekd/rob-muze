from django.contrib.auth.models import User
from django.db import models



class AnkietaOtw(models.Model):
    title = models.CharField(max_length=40)
    title_en = models.CharField(max_length=40, blank = True)
    question = models.TextField(max_length=500)
    question_en = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title



class OdpowiedzOtw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ankietaotw = models.ForeignKey(AnkietaOtw, on_delete=models.CASCADE)
    answer = models.TextField(max_length=700)
    answer_en = models.TextField(max_length=700, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.ankietaotw.title}"