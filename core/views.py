from django.shortcuts import render
from .forms import SignupForm, SignupForm2
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from account.models import Account
from collabs.models import CollabSub
from django.core.mail import EmailMessage
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from.tokens import account_activation_token
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from core.forms import emailUpdate


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

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
        
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Twoje konto zostalo pomyslnie aktywowane! Mozesz sie zalaogowac.')
        return redirect('core:login')
    else:
        messages.error(request, 'Link aktywacyjny nie dziala poprawnie.')
        return redirect('core:index')

def activateEmail(request, user, to_email):
    mail_subject = 'Aktywoj swoje konto na RobMuze.pl'
    message = render_to_string('template_activate_acc.html', {
        'user' : user.username,
        'domain' : get_current_site(request).domain,
        'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
        'token' : account_activation_token.make_token(user),
        'protocol' : 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to your email <b>{to_email}</b> and click on the activation link in order to activate your account.')
    else:
        messages.error(request, f'cos sie spierdolilo. sprawdz czy {to_email} to poprawny adres email')

def signup(request):
    if request.method == 'POST':
        form = SignupForm2(request.POST)
        if form.is_valid():
            user = get_user_model().objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                is_active=False,
            )
            user.set_password(form.cleaned_data['password1'])
            user.save()
            account = Account.objects.create(user=user)
            account.profesja = form.cleaned_data.get('profesja')
            account.save()
            
            activateEmail(request, user, form.cleaned_data.get('email'))
            
            return redirect('/')
    else:
        form = SignupForm2()

    return render(request, 'core/signup.html', {
        'form' : form
    })

    
    
@login_required
def profil(request):

    user = request.user
    profil = Account.objects.filter(user=user).first()
    collabs = CollabSub.objects.filter(user=user)

    context = {
        'user': user,
        'profil':profil,
        'collabs' : collabs
    }

    return render(request, 'core/dash.html', context)





def editEmail(request):
    if request.method == 'POST':
        emailForm = emailUpdate(request.POST, 
                                # request.FILES,
                                instance=request.user)
        
        if emailForm.is_valid():
            emailForm.save()
            messages.success(request, "Email Zaaktualizowany!")
            return redirect(to='core:profil')
    else:
        emailForm = emailUpdate(instance=request.user)
        
    return render(request, 'core/editmail.html', {"emailForm" : emailForm})