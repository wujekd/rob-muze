from django.shortcuts import render
from .forms import SignupForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from account.models import Account


# Create your views here.


def index(request):
    # items = Item.objects.filter(is_sold=False)[0:6]
    # categories = Category.objects.all()

    return render(request, 'core/index.html',
    #               {
    #     'categories' : categories,
    #     'items' : items,
    # }
                  )



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form' : form
    })
    
    
    
    
@login_required
def profil(request):
    # Access the authenticated user object using 'request.user'
    user = request.user
    profil = Account.objects.filter(user=user).first()

    # You can add more data to the context if needed
    context = {
        'user': user,
        'profil':profil,
    }

    return render(request, 'core/dash.html', context)