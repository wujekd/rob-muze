from django.shortcuts import render
from . models import Ideas
from . forms import AddIdeaForm




def ideas(request):
    ideas = Ideas.objects.all()
    return render(request, 'ideas/ideas.html', {
        'ideas' : ideas,
        
    })
    
    

def add_idea(request):
    form = AddIdeaForm()
    
    return render(request, "ideas/add-idea.html",{
        'form' : form,
        
    })