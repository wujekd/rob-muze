from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.utils.translation import gettext as _

from account.models import Account

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder ' : 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder ' : 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    


# class SignupForm(UserCreationForm):
#     cokolwiek = forms.CharField(widget=forms.TextInput, max_length=34, required=False)
    
#     class Meta:
#         model = User
#         fields = ('username', 'cokolwiek', 'email', 'password1', 'password2')
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder ' : 'Your username',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
    
#     email = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder ' : 'Your email',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder ' : 'Your password',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder ' : 'Repeat your password',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         count = User.objects.filter(email=email).count()
#         print(count)
#         if count > 0:
#             raise forms.ValidationError('Ten adres email jest juz zajety!')
#         return email


class SignupForm2(forms.Form):
    PROFESJA_CHOICES = [
        ('Wybierz', 'Wybierz'),
        ('Wokal/Inst', 'Wokal/Inst'),
        ('Produkcja', 'Produkcja'),
        ('Zadnej pracy sie nie boje', 'Zadnej pracy sie nie boje'),
    ]
    
    profesja = forms.ChoiceField(
        choices=PROFESJA_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full py-4 px-6 rounded-xl  blk-txt',
        })
    )
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': _('Username'),
        'class': 'w-full py-3 px-6 rounded-xl blk-txt' }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
        'class': 'w-full py-3 px-6 rounded-xl blk-txt'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Password'),
        'class': 'w-full py-3 px-6 rounded-xl blk-txt'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Confirm Password'),
        'class': 'w-full py-3 px-6 the rounded-xl blk-txt'}))
    
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    captcha = ReCaptchaField(
    widget=ReCaptchaV2Checkbox(),
    error_messages={
        'required': _('Udowodnij ze nie jestes robotem, zarejestruj sie potem.'),
    }
)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError(_('Hasla do siebie nie pasuja.'))
        return password2
    def clean_profesja(self):
        profesja = self.cleaned_data.get('profesja')
        if profesja == 'Wybierz':
            raise forms.ValidationError('Wybierz z listy czym zajmujesz sie w muzyce!')
        return profesja
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        count = User.objects.filter(email=email).count()
        print(count)
        if count > 0:
            raise forms.ValidationError('Ten adres email jest juz zajety!')
        return email
    
    
    
class emailUpdate(forms.ModelForm):
    email = forms.EmailField(required=True,
                                widget=forms.TextInput(attrs={'class' : 'accForm'}))
    
    class Meta:
        model = User
        fields = ['email']
        
        