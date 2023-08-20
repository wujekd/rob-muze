from django.shortcuts import render, redirect
from .models import Collab, CollabSub, Voting, Vote
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
        


def votings(request):
    votings = Voting.objects.all()
    
    return render(request, 'collabs/votings.html', {
        'votings' : votings
    })
    
def voting(request, pk):
    voting = Voting.objects.get(pk=pk)
    collab = Collab.objects.get(pk=voting.collab.id)
    subs = CollabSub.objects.filter(collab=collab)
    vote_count = Vote.objects.filter(voting=voting).count()
    
    return render(request, 'collabs/voting.html', {
        'voting' : voting,
        'collab' : collab,
        'subs' : subs,
        'vote_count' : vote_count
    })


def vote(request, pk):
    
    if request.method == 'POST':
        voter_ip = request.META.get('REMOTE_ADDR')
        if #no ip in votes then:
            id = request.POST.get('submission_id')
            sub = CollabSub.objects.get(pk=id)
            voting = Voting.objects.get(collab=sub.collab)
            
            vote = Vote.objects.create(vote_on=sub, voting=voting, voter_ip=voter_ip)
            vote.save()
            
            return redirect('collabs:votings')
        
        else:
            pass
            #u already voted
        
    
    else:
        sub = CollabSub.objects.get(pk=pk)
        
        return render(request, 'collabs/vote.html', {
            'sub' : sub
        })