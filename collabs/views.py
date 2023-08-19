from django.shortcuts import render, redirect
from .models import Collab

def collabs(request):
    collabs = Collab.objects.all()
    return render(request, 'collabs/collabs.html', {
        'collabs' : collabs,
    })

def collab(request, pk):
    collab = Collab.objects.get(pk=pk)
    
    return render(request, 'collabs/collab.html', {
        'collab' : collab
    })

# create the form 