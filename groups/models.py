from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=75)
    desc = models.TextField(max_length=420)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_groups')
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
    joined = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'group')