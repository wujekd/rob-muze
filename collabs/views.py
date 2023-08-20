from django.shortcuts import render, redirect
from .models import Collab, CollabSub
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
    
    if request.method == 'POST':
        collab_id = collab.id
        title = request.POST.get('title')
        description = request.POST.get('msg')
        file = request.FILES.get('file')
        
        # Create a new CollabSub instance and associate it with the collab_id
        collab_sub = CollabSub.objects.create(
            user=request.user,
            collab_id=collab_id,
            title=title,
            msg=description,
            file=file
        )
        collab_sub.save()
        return redirect('core:index')
    
    else:
        form = CollabSubform
        
        return render(request, 'collabs/collab_submit.html', {
            'collab' : collab,
            'form' : form,
    })