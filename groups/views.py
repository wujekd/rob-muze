from django.shortcuts import render, get_object_or_404
from .models import Group
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
    print(collabs)
    
    context = { "group" : group, 'members' : members, 'collabs' : collabs }
    
    return render(request, 'groups/group.html', context)