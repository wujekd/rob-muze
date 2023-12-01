from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    profesja = models.CharField(max_length=30, blank=True, null=True,
                                              choices =[('Wokal/Inst', 'Wokal/Inst'), ('Produkcja', 'Produkcja'),
                                                        ('Zadnej pracy sie nie boje', 'Zadnej pracy sie nie boje')])
    def __str__(self):
        return self.user.username
    