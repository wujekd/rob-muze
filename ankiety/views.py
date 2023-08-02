from django.shortcuts import render
from .forms import AnkietaOtw_form
from .models import AnkietaOtw, OdpowiedzOtw
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def ankiety(request):
    # ankiety = AnkietaOtw.objects.all()
    # odpowiedzi = OdpowiedzOtw.objects.filter(user=request.user)
    # answered = []
    # unanswered =[] 
    # for odpowiedz in odpowiedzi:
    #     if odpowiedz.ankietaotw in ankiety:
    #         answered.append(odpowiedz.ankietaotw)
    # for pytanie in ankiety:
    #     if pytanie not in answered:
    #         unanswered.append(pytanie)
    
    ankiety = AnkietaOtw.objects.annotate(num_answer=Count('odpowiedzotw',
                                                 filter=Q(odpowiedzotw__user=request.user)))
    answered = ankiety.filter(num_answer__gt=0)
    unanswered = ankiety.filter(num_answer=0)
    
        
    print(answered)
    print(unanswered)
    return render(request, 'ankiety/ankiety.html', {
        'answered' : answered,
        'unanswered' : unanswered,
    })




@login_required
def ankietaotw(request, pk):
    pytanie = get_object_or_404(AnkietaOtw, pk=pk)
    if request.method == 'POST':
        ankieta = AnkietaOtw_form(request.POST)
        if ankieta.is_valid():
            odpowiedz = ankieta.save(commit=False)
            odpowiedz.ankietaotw = pytanie
            odpowiedz.user = request.user
            odpowiedz.save()
            
            user_acc = Account.objects.get(user=request.user)
            user_acc.points += 120
            user_acc.save()
            
            return redirect('ankiety:ankiety')
            
    else:
        odpowiedz = OdpowiedzOtw.objects.filter(user=request.user, ankietaotw=pytanie)
    
    if odpowiedz:
        return render(request, 'ankiety/answered.html', {
            'ankieta' : odpowiedz,
            'odpowiedz' : odpowiedz,
        })
    
    else:
        form = AnkietaOtw_form()
        
        return render(request, 'ankiety/ankietaotw.html', {
            'form' : form,
            'ankieta' : pytanie,
        })