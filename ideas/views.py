from django.shortcuts import render, redirect
from . models import Ideas
from . forms import AddIdeaForm
from django.contrib.auth.decorators import login_required





def ideas(request):
    ideas = Ideas.objects.all()
    return render(request, 'ideas/ideas.html', {
        'ideas' : ideas,
        
    })
    
    
@login_required
def add_idea(request):
    if request.method == "POST":
        form = AddIdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = request.user  # Set the user field
            idea.save()
            return redirect('core:profil') 
        else:
            return render(request, "ideas/add-idea.html", {
                'form': form,
            })
    else:
        form = AddIdeaForm()
    
    return render(request, "ideas/add-idea.html", {
        'form': form,
    })