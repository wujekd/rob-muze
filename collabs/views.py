from django.shortcuts import render, redirect
from .models import Collab, CollabSub, Voting, Vote
from .forms import CollabSubform
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta

def collabs(request):
    collabs = Collab.objects.all()
    active_votings = Voting.objects.filter(active = True)
    # for voting in active_votings:
    #     voting.tags_list = voting.tags.split(',')
        
    return render(request, 'collabs/collabs.html', {
        'collabs' : collabs,
        'votings' : active_votings,
    })



def collab(request, pk):
    collab = Collab.objects.get(pk=pk)
    submission_count = CollabSub.objects.filter(collab=pk).count()
    print(submission_count)
    deadline = collab.date + timedelta(weeks=4)
    time = deadline - timezone.now()
    
    return render(request, 'collabs/collab.html', {
        'collab' : collab,
        "submission_count" : submission_count,
        "time": time.total_seconds(),
    })




def przeslij(request, pk):
    collab = Collab.objects.get(pk=pk)
    form = CollabSubform(request.POST, request.FILES)
    
    if request.method == 'POST':
        collab_id = collab.id
        title = request.POST.get('title')
        description = request.POST.get('msg')
        file = request.FILES.get('file')
        
        if form.is_valid():
            collab_sub = CollabSub.objects.create(
                user=request.user,
                collab_id=collab_id,
                title=title,
                msg=description,
                file=file
            )
            collab_sub.save()
            return redirect('core:profil')
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
        id = request.POST.get('submission_id')
        sub = CollabSub.objects.get(pk=id)
        voting = Voting.objects.get(collab=sub.collab)
        #
        # ip_check = Vote.objects.filter(voting=voting, voter_ip=voter_ip).exists()
        ip_check = False
        if not ip_check:
            vote = Vote.objects.create(vote_on=sub, voting=voting, voter_ip=voter_ip)
            vote.save()
            
            print('IP CHECK PASSED - VOTE SAVED')

            return render(request, 'collabs/voted.html', {
                'vote_success' : True
                #pass what voted on
            })
        
        else:
            print('IP CHECK ERROR')
            return render(request, 'collabs/voted.html', {
                'vote_success' : False
            })
        
    
    else:
        sub = CollabSub.objects.get(pk=pk)
        
        return render(request, 'collabs/vote.html', {
            'sub' : sub
        })