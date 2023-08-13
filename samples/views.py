from django.shortcuts import render, redirect
from .models import Sampel, Downloads
from django.http import FileResponse
from account.models import Account
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


# Create your views here.

def samples(request):
    sample = Sampel.objects.all()
    
    if request.user.is_authenticated:
        
        user_acc = Account.objects.get(user=request.user)
        points = user_acc.points
        
        return render(request, 'samples/samples.html', {
            'sample' : sample,
            'points' : points,
        })
    else:
        return render(request, 'samples/samples.html', {
            'sample' : sample,
        })
        
    
def sample_detail(request, pk):
    sampel = get_object_or_404(Sampel, pk=pk)
    
    return render(request, 'samples/sampledetail.html', {
        'sample' : sampel
    })
    

def download_file(request, pk):
    
    sampel = Sampel.objects.get(pk=pk)
    
    user = request.user
    user_acc = Account.objects.get(user=user)
    
    # check if downloaded
    if Downloads.objects.filter(user=user, sample=sampel).exists():
        download = Downloads.objects.get(user=user, sample=sampel)
        return render(request, 'samples/already_downloaded.html', {
            'download' : download
        })
    
    # check if enough points
    if user_acc.points >= sampel.cena:
        user_acc.points -= sampel.cena
        user_acc.save()
        
        file_path = Sampel.objects.get(pk=pk).mp3_file.url
        file_path = file_path[1:]

        file = open(file_path, 'rb')
        response = FileResponse(file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{file_path.split("/")[-1]}"'
        
        messages.add_message(request, messages.SUCCESS, 'Pobrano ' + sampel.title + '!', extra_tags='bg-green-800')
        # Downloads.objects.create(user=user, sample=sampel)
        
        return response
    
    else:
        return render(request, 'samples/no_points.html', {
            'points' : user_acc.points,
            'sampel' : sampel
        })

    
def message(request):
    messages.add_message(request, messages.INFO, 'Test message', extra_tags='bg-green-800')
    return redirect('/sample')