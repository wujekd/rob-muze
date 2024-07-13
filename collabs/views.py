from django.shortcuts import render, redirect
from .models import Collab, CollabSub, Stages, Vote, PackDownloads
from account.models import Account
from .forms import CollabSubform, SubCheckForm
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.http import FileResponse
import mimetypes
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.conf import settings
import os
from django.db.models import Prefetch, Q


def collabs(request):
    collabs = Collab.objects.all()
    # active_votings = Voting.objects.filter(active = True)
    # for voting in active_votings:
    #     voting.tags_list = voting.tags.split(',')
        
    return render(request, 'collabs/collabs.html', {
        'collabs' : collabs,
        # 'votings' : active_votings,
    })
    
    

def collab(request, pk):
    user = request.user
    collab = Collab.objects.get(pk=pk)
    deadline = collab.date + timedelta(weeks=4)
    time = int((deadline - timezone.now()).total_seconds())
    
    stages = Stages.objects.filter(collab=collab)
    
    context = {
        'collab' : collab,
    }
    
    if len(stages) == 1:
        current_stage = stages.last()
        time = int((current_stage.deadline - timezone.now()).total_seconds())
        download_count = PackDownloads.objects.filter(stage=current_stage).count()
        subs = CollabSub.objects.filter(stage=current_stage)
        vote_count = len(subs)
        context.update({
            "download_count" : download_count,
            "time": time,
            
        'subs' : subs,
        'vote_count' : vote_count,
        })
        
    elif len(stages) > 1:
        past_stages = stages.exclude(pk=current_stage.pk)
    
    

    

    
    
    if request.user.is_authenticated:
        submitted = False
        if PackDownloads.objects.filter(stage=pk, user=user):
            downloaded = True
            if CollabSub.objects.filter(stage=pk, user=user):
                submitted = True
        else:
            downloaded = False
        
        context.update({
            'downloaded' : downloaded,
            'submitted' : submitted,
        })

    return render(request, 'collabs/collab.html', context)


                                 # VOTING
def voting(request, pk):
    voting = Voting.objects.get(pk=pk)
    collab = Collab.objects.get(pk=voting.collab.id)
    subs = CollabSub.objects.filter(collab=collab)
    vote_count = Vote.objects.filter(voting=voting).count()
    downloaded = False
    
    
    if request.user.is_authenticated:
        downloaded = ()
    
    deadline = voting.date + timedelta(weeks=1)
    time = int((deadline - timezone.now()).total_seconds())
    
        
    return render(request, 'collabs/voting.html', {
        'voting' : voting,
        'collab' : collab,
        'subs' : subs,
        "time" : time,
        'vote_count' : vote_count,
        "downloaded" : downloaded,
    })

    
    
    
def collab_pack_download(request, pk):
    
    collab = Collab.objects.get(pk=pk)
    
    user = request.user
    # user_acc = Account.objects.get(user=user)
    account = request.user.account
    
    if PackDownloads.objects.filter(user=user, collab=collab):
        return redirect('core:profil')
        
    # check if enough points
    if account.points >= 30:
        account.points - 30
        account.save()
    
        file_path = Collab.objects.get(pk=pk).download_pack.url
        file_path = file_path[1:]
        
        content_type, _ = mimetypes.guess_type(file_path)
        if not content_type:  # If mimetypes fails to guess, go back to octet-stream
            content_type = 'application/octet-stream'
            
        file = open(file_path, 'rb')

        response = FileResponse(file, content_type=content_type)

        response['Content-Disposition'] = f'attachment; filename="{file_path.split("/")[-1]}"'
        download_record = PackDownloads.objects.create(collab=collab, user=user)
        download_record.save()
        
        messages.add_message(request, messages.SUCCESS, 'Pobrano ' + collab.title + '!', extra_tags='bg-secondary')
        
        return response
    
    else:
        return render(request, 'samples/no_points.html', {
            'points' : account.points,
            'sample' : collab
        })


from django.http import JsonResponse

def przeslij(request, pk):
    user = request.user
    collab = Collab.objects.get(pk=pk)
    # if CollabSub.objects.filter(user=user, collab=collab):
    #     return redirect('core:profil') 
        # !!!^
    form = CollabSubform(request.POST, request.FILES)
    # ??? can i just put pk instead of collab.id if collab pk=pk
    if request.method == 'POST':
        collab_id = collab.id
        title = request.POST.get('title')
        msg = request.POST.get('msg')
        file = request.FILES.get('file')
        volOffset = request.POST.get("volumeOffset")
        
        if form.is_valid():
            collab_sub = CollabSub.objects.create(
                user=user,
                collab_id=collab_id,
                title=title,
                msg=msg,
                file=file,
                volumeOffset = volOffset
            )
            collab_sub.save()
            with open('submissions_to_render_demos.txt', 'a') as f:
                f.write(f"{collab_sub.id},{collab_sub.file.path}\n")
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = CollabSubform
    
    return render(request, 'collabs/collab_submit.html', {
        'collab' : collab,
        'form' : form,
})



def unchecked(request):
    # unapproved_responses = CollabSub.objects.filter(Q(approved=False) | Q(approved__isnull=True), demoCreated=True)
    unapproved_responses = CollabSub.objects.filter(Q(approved=False) | Q(approved__isnull=True))
    collabs_with_unapproved_responses = Collab.objects.prefetch_related(
        Prefetch('responses', queryset=unapproved_responses, to_attr='unapproved_responses')
    )
    # Filter songs that have unapproved responses
    collabs_with_unapproved_responses = [collab for collab in collabs_with_unapproved_responses if collab.unapproved_responses]
    print('collabs with no responses: ', collabs_with_unapproved_responses)
    # Pass the data to the template
    context = {
        'collabs': collabs_with_unapproved_responses
    }
    return render(request, "collabs/checksubmissions.html", context)




def check(request, pk):
    response = get_object_or_404(CollabSub, pk=pk)
    collab = response.collab

    if request.method == 'POST':
        form = SubCheckForm(request.POST, instance=response)
        if form.is_valid():
            form.save()
            print("form valid")
            return redirect('unchecked') 
    else:
        form = SubCheckForm(instance=response)

    context = {
        'response': response,
        'collab': collab,
        'form': form
    }
    return render(request, 'collabs/check-sub.html', context)





                                # VOTINGS
def votings(request):
    votings = Voting.objects.all()
    
    return render(request, 'collabs/votings.html', {
        'votings' : votings
    })
    






def vote(request, pk):
    if request.method == 'POST':
        voter_ip = request.META.get('REMOTE_ADDR')
        id = request.POST.get('submission_id')
        sub = CollabSub.objects.get(pk=id)
        voting = Voting.objects.get(collab=sub.collab)
        #
        ip_check = Vote.objects.filter(voting=voting, voter_ip=voter_ip).exists()
        # ip_check = False
        if not ip_check:
            vote = Vote.objects.create(vote_on=sub, voting=voting, voter_ip=voter_ip)
            vote.save()
            
            print('IP CHECK PASSED - VOTE SAVED')

            return render(request, 'collabs/voted.html', {
                'vote_success' : True,
                'voted_on' : sub
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