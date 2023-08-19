from django.shortcuts import render, redirect
from .models import Collab
from .forms import CollabSubform

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

def przeslij(request, pk):
    collab = Collab.objects.get(pk=pk)
    
    form = CollabSubform
    
    return render(request, 'collabs/collab_submit.html', {
        'collab' : collab,
        'form' : form,
    })