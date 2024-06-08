from django.shortcuts import render
from .forms import SignupForm2
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
from core.forms import emailUpdate, profilePicForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.views import View
from django.utils import translation
from django.utils.translation import gettext as _
from django.utils.translation import get_language

    
class SetLang(View):
    def post(self, request):
        language = request.POST.get('language')
        translation.activate(language)
        request.session['django_language'] = language
        return redirect(request.POST.get('next', 'core:index'))


# Create your views here.

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = './core/password.html'
    success_message = "Haslo zostalo zmienione!"
    success_url = reverse_lazy('core:profil')


def index(request):
    from django.utils import translation
    # user_language = 'en'
    # translation.activate(user_language)
    # request.session['django_language'] = user_language
    
    if 'django_language' in request.session:
        del request.session['django_language']
        print("deleted session key")

    return render(request, 'core/index.html')


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
    lnag = get_language()
    policy_file = 'core/policy_pl.txt' if lnag == 'pl' else 'core/policy_en.txt'
    with open(policy_file, 'r') as file:
        policy = file.read()
    if request.method == 'POST':
        form = SignupForm2(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            offensive_words = ['kurwa', 'skurwiel', 'chuj']
            if any(word in username for word in offensive_words):
                form.add_error('username', "Nazwa uzytkownika nie moze zawierac wulgarnych slow, chamie.")
                return render(request, "core/signup.html", {"form" : form})
            if User.objects.filter(username=username).exists():
                form.add_error('username', "Ta nazwa uzytkownika jest juz zajeta")
                return render(request, "core/signup.html", {"form" : form, "policy" : policy})
            
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
        'form' : form, 'policy' : policy
    })



@login_required
def profil(request):

    user = request.user
    # profil = Account.objects.filter(user=user).first() -needs .first cos a query set
    profil = user.account
    collabs = CollabSub.objects.filter(user=user)
    context = {
        'user': user,
        'profil':profil,
        'collabs' : collabs
    }

    return render(request, 'core/dash.html', context)



def editEmail(request):
    if request.method == 'POST':
        emailForm = emailUpdate(request.POST, instance=request.user)
        if emailForm.is_valid():
            emailForm.save()
            messages.success(request, "Email Zaaktualizowany!")
            return redirect('core:profil')
    else:
        emailForm = emailUpdate(instance=request.user)

    # Add this line to display form errors in the template
    errors = emailForm.errors.as_data() if emailForm.errors else None
    
    return render(request, 'core/editmail.html', {"emailForm" : emailForm, "errors": errors})

def profilePic(request):
    account = request.user.account
    if request.method == 'POST':
        form = profilePicForm(request.POST, 
                                request.FILES,
                                instance=account)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Obrazek Profilowy Zaaktualizowany!")
            return redirect(to='core:profil')
    else:
        form = profilePicForm(instance=account)
        
    return render(request, 'core/profilePic.html', 
                  {"form" : form,
                   "profil" : account})