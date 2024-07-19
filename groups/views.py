from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Group, MembershipRequest, GroupMembership, Invitation
from collabs.models import Collab
from .forms import VerifyMemberForm, JoinGroupForm
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.utils.crypto import get_random_string

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
    membership_request = MembershipRequest.objects.get(pk=pk)
    member = request.user
    
    if request.method == "POST":
        form = VerifyMemberForm(request.POST)
        if form.is_valid():
            approve = form.cleaned_data['approve']
            if approve:
                GroupMembership.objects.create(
                    user=membership_request.user,
                    group=membership_request.group,
                    role='user'  # or whatever role you want to assign
                )
            # Delete the membership request after processing
            membership_request.delete()
            return redirect('groups:group', pk=membership_request.group.pk)
    else:
        form = VerifyMemberForm()

    return render(request, 'groups/verify.html', {'form': form, 'membership_request': membership_request})




def join_group(request, pk):
    
    group = get_object_or_404(Group, pk=pk)
    
    if request.method == "POST":
        user = request.user
        if GroupMembership.objects.filter(group=group, user=user).exists():
            return JsonResponse({'success': False, 'message': 'You are already a member of this group.'})

        if MembershipRequest.objects.filter(group=group, user=user).exists():
            return JsonResponse({'success': False, 'message': 'You have already submitted a membership request for this group.'})
        
        MembershipRequest.objects.create(user=user, group=group)
        return JsonResponse({'success': True, 'message': 'Membership request added'})
    
    

    
@login_required
def join_group_with_token(request, token):
    invitation = get_object_or_404(Invitation, token=token, used_by__isnull=True)
    group = invitation.group
    

    if GroupMembership.objects.filter(group=group, user=request.user).exists():
        messages.error(request, 'You are already a member of this group.')
        return redirect('groups:group', pk=group.id)
    

    GroupMembership.objects.create(user=request.user, group=group, role='user')
    

    invitation.used_by = request.user
    invitation.save()

    messages.success(request, 'You have joined the group.')
    return redirect('groups:group', pk=group.id)



def create_invitation(request, pk):
    group = get_object_or_404(Group, id=pk)
    
    # Create an invitation instance without manually handling the token
    invitation = Invitation(group=group)
    invitation.save()

    return JsonResponse({'token': invitation.token})













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