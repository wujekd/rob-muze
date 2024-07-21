from django.db import models
from django.contrib.auth.models import User
# from collabs.models import Stages
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
# from collabs.models import Collab, CollabSub


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
        
        
class MembershipRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='membership_requests')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    created = models.DateTimeField(auto_now_add=True)
    
    
    
    
class Invitation(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    used_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = get_random_string(length=22)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Invitation to {self.group.name} - {"Used" if self.used_by else "Unused"}'
    

