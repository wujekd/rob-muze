from django.shortcuts import render, get_object_or_404
from .models import Group, MembershipRequest
from collabs.models import Collab
# Create your views here.
def groups(request):
    groups = Group.objects.all()
    
    context = { 'groups' : groups}
    
    return render(request, 'groups/groups.html', context)


def group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    members = group.members.all()
    collabs = Collab.objects.filter(group=group)
    
    
    membership_requests = MembershipRequest.objects.filter(group=group)
    request_count = len(membership_requests)
    
    context = { "group" : group, 'members' : members, 'collabs' : collabs,
               "requests" : membership_requests, 'request_count' : request_count,
               }
    
    return render(request, 'groups/group.html', context)


def verify_member(request, pk):
    
    return render(request, "groups/verify.html")






# groups/models.py
# from django.db import models
# from django.contrib.auth.models import User
# from .utils import generate_invitation_token

# class Group(models.Model):
#     name = models.CharField(max_length=75)
#     # Other fields...

#     invitation_tokens = models.ManyToManyField(User, through='InvitationToken', related_name='group_invitations')

#     def generate_invitation_token(self, user):
#         token = generate_invitation_token()
#         InvitationToken.objects.create(group=self, user=user, token=token)
#         return token

#     def remove_invitation_token(self, token):
#         InvitationToken.objects.filter(group=self, token=token).delete()

#     def __str__(self):
#         return self.name

# class InvitationToken(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     token = models.CharField(max_length=32, unique=True)

#     def __str__(self):
#         return f"{self.group.name} - {self.user.username} - {self.token}"

# def send_invitation(request, group_id, user_id=None):
#     group = get_object_or_404(Group, pk=group_id)
#     if user_id:
#         user = get_object_or_404(User, pk=user_id)
#     else:
#         user = None

#     if request.user.is_authenticated and user == request.user:
#         token = group.generate_invitation_token(user)
#         # Send invitation logic (e.g., email or social media message)
#         # Redirect or render response as needed
#     elif user:
#         token = group.generate_invitation_token(user)
#         # Send invitation logic (e.g., email or social media message)
#         # Redirect or render response as needed
#     else:
#         # Handle case where user is not logged in or user_id is not provided
#         # Redirect or render response as needed

#     return redirect('group_detail', pk=group.pk)