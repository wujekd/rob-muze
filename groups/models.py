from django.db import models
from collabs.models import Collab
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=75)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Collab, on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(User, through='GroupMembership')

class GroupMembership(models.Model):
    USER_ROLES = [
        ('admin', 'Admin'),
        ('mod', 'Moderator'),
        ('user', 'User'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES)

class Admins(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Mods(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)