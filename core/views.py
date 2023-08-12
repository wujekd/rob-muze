from django.shortcuts import render
from .forms import SignupForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from account.models import Account
from django.core.mail import EmailMessage
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from.tokens import account_activation_token


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
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('/')
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